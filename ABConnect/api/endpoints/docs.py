from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.common import DocType, to_file_dict


class DocsEndpoint(BaseEndpoint):
    def parcel_label(self, pro) -> dict:
        docpath = f"shipment/{pro}/{pro}_Label.pdf"
        uri = "documents/get/%s" % docpath
        response = self._r.call("GET", uri, raw=True)
        return to_file_dict(
            response,
            pro,
            "Label",
        )

    def get(self, jobid) -> dict:
        """List the documents for a job."""
        url_params = {"jobDisplayId": jobid}
        return self._r.call("GET", "documents/list", params=url_params)

    def download(self, docpath) -> dict:
        """Download a document."""
        return self._r.call("GET", f"documents/get/{docpath}")

    def upload(self, jobid, files, data=None) -> dict:
        """Upload documents to a job."""
        url = f"documents/upload/{jobid}"
        return self._r.upload_file(url, files)

    def upload_item_photos(self, jobid, itemid, files, rfqid=None) -> dict:
        """Upload item photos to a job."""
        data = {
            "JobDisplayId": jobid,
            "DocumentType": DocType.Item_Photo.value,
            "DocumentTypeDescription": DocType.Item_Photo.fmt,
            "Shared": 28,
            "JobItems": [itemid],
            "RfqId": rfqid,
        }
        return self._r.upload_file("documents", files=files, data=data)
