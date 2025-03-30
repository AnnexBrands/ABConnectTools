from ABConnect.api.endpoints.base import BaseEndpoint


class ItemsEndpoint(BaseEndpoint):
    def get_freight(self, jobid) -> dict:
        job_data = self._r.call("GET", f"job/{jobid}")
        return job_data["freightItems"]

    def set_freight(self, jobid, freighitems) -> dict:
        return self._r.call("POST", f"job/{jobid}/freightitems", json=freighitems)

    def get_parcel(self, jobid) -> dict:
        return self._r.call("GET", f"job/{jobid}/parcelitems")

    def set_parcel(self, jobid, parcelitems) -> dict:
        return self._r.call("POST", f"job/{jobid}/parcelitems", json=parcelitems)

    def update_parcel(self, jobid, parcelItemId, parcelitems) -> dict:
        return self._r.call(
            "PUT", f"job/{jobid}/parcelitems/{parcelItemId}", json=parcelitems
        )

    def delete_parcel(self, jobid, parcelItemId) -> dict:
        return self._r.call("DELETE", f"job/{jobid}/parcelitems/{parcelItemId}")
