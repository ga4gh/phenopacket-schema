Phenopacket schema
==================

|Build Status| |Maven Central| |Documentation|

.. |Build Status| image:: https://travis-ci.org/phenopackets/phenopacket-schema.svg?branch=master
  :target: https://travis-ci.org/phenopackets/phenopacket-schema

.. |Maven Central| image:: https://maven-badges.herokuapp.com/maven-central/org.phenopackets/phenopacket-schema/badge.svg
  :target: https://maven-badges.herokuapp.com/maven-central/org.phenopackets/phenopacket-schema

.. |Documentation| image:: https://readthedocs.org/projects/phenopackets-schema/badge/?version=latest
  :target: https://phenopacket-schema.readthedocs.io/en/latest/

This has been produced as part of the `GA4GH`_ `Clinical Phenotype Data Capture Workstream`_ and it merges the existing `GA4GH metadata-schemas`_ work with a more focused model from the `phenopacket-reference-implementation`_.

.. _GA4GH: https://ga4gh.org
.. _Clinical Phenotype Data Capture Workstream: https://ga4gh-cp.github.io/
.. _GA4GH metadata-schemas: https://github.com/ga4gh-metadata/metadata-schemas
.. _phenopacket-reference-implementation: https://github.com/phenopackets/phenopacket-reference-implementation


This is a re-defined version of the original phenopacket with a more individual-centric approach. This new approach was taken in order to simplify the code required to represent and manipulate the data and also better represent this sort of data as it is in day to day use.

Documentation
=============

The core documentation can be found at `Documentation`_

The documentation in this README is primarily for the users of the phenopackets-schema java library.

.. _Documentation: https://phenopacket-schema.readthedocs.io/en/latest/index.html

Scope and Purpose
=================
The goal of the phenopacket-schema is to define the phenotypic description of a patient/sample in the context of rare disease or cancer genomic diagnosis. It aims to provide sufficient and shareable information of the data outside of the EHR (Electronic Health Record) with the aim of enabling capturing of sufficient structured data at the point of care by a clinician or clinical geneticist for sharing with other labs or computational analysis of the data in clinical or research environments.

The schema aims to define a common, limited set of data types which may be composed into more specialised types for data sharing between resources using an agreed upon common schema (as defined in base.proto).

This common schema has been used to define the 'Phenopacket' which is a catch-all collection of data types, specifically focused on representing rare-disease or cancer samples for both initial data capture and analysis. The phenopacket is designed to be both human and machine-readable, and to inter-operate with the HL7 Fast Healthcare Interoperability Resources Specification (aka FHIR®).  

Versioning
==========

The library uses semantic versioning. See https://semver.org for details.

Email list
==========
There is a low-volume mailing list for announcements about phenopackets at phenopackets@groups.io. More information
about this list is available at https://groups.io/g/phenopackets.


Usage
=====
The Phenopacket schema is defined using `Protobuf`_ which is `"a language-neutral, platform-neutral extensible mechanism for serializing structured data"`.  There are two ways to use this library, firstly using the ``Phenopacket`` as an exchange mechanism, secondly as a schema of basic types on which to build more specialist messages, yet allow for easy interoperability with other resources using the phenopackets schema.

.. _Protobuf: https://developers.google.com/protocol-buffers/

Java people can incorporate phenopackets-api into their code by importing the jar using maven:

.. code:: xml

    <dependency>
        <groupId>org.phenopackets</groupId>
        <artifactId>phenopacket-schema</artifactId>
        <version>${phenopacket-schema.version}</version>
    </dependency>

The following sections describe how to achieve these two things.

Exchanging Phenopackets directly
--------------------------------
Examples on how these can be used can be found in the test directory. There are no explicit relationships defined between fields in the phenopacket (apart from the Pedigree), so it is vital that resources exchanging phenopackets agree on what is valid and what the fields mean in relation to other fields in the phenopacket. For example the ``Phenopacket.genes`` field may be agreed upon as representing the genes for a gene panel in one context, or a set of candidate genes or perhaps a diagnosed causative gene.

JSON/YAML formats
-----------------
A Phenopacket can be transformed between the native binary format and JSON using the ``JsonFormat`` class from the ``protobuf-java-util`` library. This will also need to be added to your pom.xml

.. code:: xml

    <dependency>
        <groupId>com.google.protobuf</groupId>
        <artifactId>protobuf-java-util</artifactId>
        <version>${protobuf.version}</version>
    </dependency>


``protobuf-java-util`` contains simple utility methods to perform these transformations. Usage is shown here:

.. code-block:: java

    // Transform a Phenopacket into JSON
    Phenopacket original = TestExamples.rareDiseasePhenopacket();

    String asJson = JsonFormat.printer().print(original);
    System.out.println(asJson);

    // Convert the JSON back to a Phenopacket
    Phenopacket.Builder phenoPacketBuilder = Phenopacket.newBuilder();
    JsonFormat.parser().merge(jsonString, phenoPacketBuilder);
    Phenopacket fromJson = phenoPacketBuilder.build();

    // Convert the JSON into YAML (using Jackson)
    JsonNode jsonNodeTree = new ObjectMapper().readTree(jsonString);
    String yamlPhenopacket = new YAMLMapper().writeValueAsString(jsonNodeTree);

    // Convert the YAML back into JSON (using Jackson)
    JsonNode jsonNodeTree = new YAMLMapper().readTree(yamlString);
    String jsonPhenopacket = new ObjectMapper().writeValueAsString(jsonNodeTree);

    // And finally back into a Java object
    Phenopacket.Builder phenoPacketBuilder2 = Phenopacket.newBuilder();
    JsonFormat.parser().merge(jsonPhenopacket, phenoPacketBuilder2);
    Phenopacket fromJson2 = phenoPacketBuilder2.build();

Building new messages from the schema
-------------------------------------
There is an example of how to do this included in the `mme.proto`_ file. Here the Matchmaker Exchange (MME) API has been implemented using the phenopackets schema, defining custom messages as required, but re-using messages from `base.proto`_ where applicable. Using the above example, perhaps the ``Phenopacket.genes`` is a problem as you wish to record not only the gene panels ordered, but also the candidate genes discovered in two separate fields. In this case, a new bespoke message could be created, using the ``Gene`` as a building block.

.. _mme.proto: https://github.com/phenopackets/phenopacket-schema/blob/master/src/test/proto/org/matchmakerexchange/api/v1/mme.proto
.. _base.proto: https://github.com/phenopackets/phenopacket-schema/blob/master/src/main/proto/org/phenopackets/schema/v1/core/base.proto
Building
========
The project can be built using the awesome `Takari maven wrapper`_ which requires no local maven installation. The only requirement for the build is to have a working java installation and network access.

To do this ``cd`` to the project root and run the wrapper scripts:
                                                    
.. code:: bash

    $ ./mvnw clean install

or

.. code:: cmd

    $ ./mvnw.cmd clean install


.. _Takari maven wrapper: https://github.com/takari/maven-wrapper

Sign artefacts for release
==========================
There is a ``release-sign-artifacts`` profile which can be triggered with the command

.. code:: bash

    $ ./mvnw clean install -DperformRelease=true

Java, Python and C++ artefacts
==============================
Building the project will automatically compile Java, Python and C++ artefacts. The Java jar file can be directly used in any Java project. For Python or C++ the build artefacts can be found at

.. code:: bash

    target/generated-sources/protobuf/python

and

.. code:: bash

    target/generated-sources/protobuf/cpp

Other languages will need to compile the files in ``src/main/proto`` to
their desired language. The protobuf developer site has examples on how
to do this, e.g `GO`_ or `C#`_. Protobuf also supports a `host of other
languages`_.

.. _GO: https://developers.google.com/protocol-buffers/docs/gotutorial#compiling-your-protocol-buffers
.. _C#: https://developers.google.com/protocol-buffers/docs/csharptutorial#compiling-your-protocol-buffers
.. _host of other languages: https://github.com/google/protobuf/tree/v3.7.0#protobuf-runtime-installation
