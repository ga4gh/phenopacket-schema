import os

import pytest


from google.protobuf.json_format import Parse


class TestV1IO:
    @pytest.fixture(scope="class")
    def fpath_v1_data(
        self,
        fpath_test_data_dir: str,
    ) -> str:
        return os.path.join(
            fpath_test_data_dir,
            "v1",
        )

    def test_phenopacket(
        self,
        fpath_v1_data: str,
    ):
        from phenopackets.schema.v1.phenopackets_pb2 import Phenopacket

        phenopacket_pb = Phenopacket()
        with open(os.path.join(fpath_v1_data, "phenopacket.pb"), "rb") as fh:
            phenopacket_pb.ParseFromString(fh.read())

        with open(os.path.join(fpath_v1_data, "phenopacket.json"), "rb") as fh:
            phenopacket_json = Parse(fh.read(), message=Phenopacket())

        assert phenopacket_pb == phenopacket_json

    def test_family(
        self,
        fpath_v1_data: str,
    ):
        from phenopackets.schema.v1.phenopackets_pb2 import Family

        family_pb = Family()
        with open(os.path.join(fpath_v1_data, "family.pb"), "rb") as fh:
            family_pb.ParseFromString(fh.read())

        with open(os.path.join(fpath_v1_data, "family.json"), "rb") as fh:
            family_json = Parse(fh.read(), message=Family())

        assert family_pb == family_json

    def test_cohort(
        self,
        fpath_v1_data: str,
    ):
        from phenopackets.schema.v1.phenopackets_pb2 import Cohort

        cohort_pb = Cohort()
        with open(os.path.join(fpath_v1_data, "cohort.pb"), "rb") as fh:
            cohort_pb.ParseFromString(fh.read())

        with open(os.path.join(fpath_v1_data, "cohort.json"), "rb") as fh:
            cohort_json = Parse(fh.read(), message=Cohort())

        assert cohort_pb == cohort_json


class TestV2IO:
    @pytest.fixture(scope="class")
    def fpath_v2_data(
        self,
        fpath_test_data_dir: str,
    ) -> str:
        return os.path.join(
            fpath_test_data_dir,
            "v2",
        )

    def test_phenopacket(
        self,
        fpath_v2_data: str,
    ):
        from phenopackets.schema.v2.phenopackets_pb2 import Phenopacket

        phenopacket_pb = Phenopacket()
        with open(os.path.join(fpath_v2_data, "phenopacket.pb"), "rb") as fh:
            phenopacket_pb.ParseFromString(fh.read())

        with open(os.path.join(fpath_v2_data, "phenopacket.json"), "rb") as fh:
            phenopacket_json = Parse(fh.read(), message=Phenopacket())

        assert phenopacket_pb == phenopacket_json

    def test_family(
        self,
        fpath_v2_data: str,
    ):
        from phenopackets.schema.v2.phenopackets_pb2 import Family

        family_pb = Family()
        with open(os.path.join(fpath_v2_data, "family.pb"), "rb") as fh:
            family_pb.ParseFromString(fh.read())

        with open(os.path.join(fpath_v2_data, "family.json"), "rb") as fh:
            family_json = Parse(fh.read(), message=Family())

        assert family_pb == family_json

    def test_cohort(
        self,
        fpath_v2_data: str,
    ):
        from phenopackets.schema.v2.phenopackets_pb2 import Cohort

        cohort_pb = Cohort()
        with open(os.path.join(fpath_v2_data, "cohort.pb"), "rb") as fh:
            cohort_pb.ParseFromString(fh.read())

        with open(os.path.join(fpath_v2_data, "cohort.json"), "rb") as fh:
            cohort_json = Parse(fh.read(), message=Cohort())

        assert cohort_pb == cohort_json
