from django.core.exceptions import ObjectDoesNotExist
from djblets.webapi.errors import DOES_NOT_EXIST

from reviewboard.webapi.decorators import webapi_check_local_site
from reviewboard.webapi.resources import resources
from reviewboard.webapi.resources.base_diff_comment import \
    BaseDiffCommentResource


class FileDiffCommentResource(BaseDiffCommentResource):
    """Provides information on comments made on a particular per-file diff.

    The list of comments cannot be modified from this resource. It's meant
    purely as a way to see existing comments that were made on a diff. These
    comments will span all public reviews.
    """
    allowed_methods = ('GET',)
    model_parent_key = 'filediff'
    uri_object_key = None

    mimetype_list_resource_name = 'file-diff-comments'
    mimetype_item_resource_name = 'file-diff-comment'

    def get_queryset(self, request, review_request_id, diff_revision,
                     filediff_id, *args, **kwargs):
        """Returns a queryset for Comment models.

        This filters the query for comments on the specified review request
        and made on the specified diff revision, which are either public or
        owned by the requesting user.

        If the queryset is being used for a list of comment resources,
        then this can be further filtered by passing ``?interdiff-revision=``
        on the URL to match the given interdiff revision, and
        ``?line=`` to match comments on the given line number.
        """
        q = super(FileDiffCommentResource, self).get_queryset(
            request, review_request_id, *args, **kwargs)
        return q.filter(filediff__diffset__revision=diff_revision,
                        filediff__id=filediff_id)

    @webapi_check_local_site
    def get_list(self, request, diff_revision=None, *args, **kwargs):
        """Returns the list of comments on a file in a diff.

        This list can be filtered down by using the ``?line=`` and
        ``?interdiff-revision=``.

        To filter for comments that start on a particular line in the file,
        using ``?line=``.

        To filter for comments that span revisions of diffs, you can specify
        the second revision in the range using ``?interdiff-revision=``.
        """
        try:
            resources.filediff.get_object(
                request, diff_revision=diff_revision, *args, **kwargs)

            return super(FileDiffCommentResource, self).get_list(
                request, diff_revision=diff_revision, *args, **kwargs)
        except ObjectDoesNotExist:
            return DOES_NOT_EXIST


filediff_comment_resource = FileDiffCommentResource()