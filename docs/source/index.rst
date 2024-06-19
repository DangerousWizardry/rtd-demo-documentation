
MIMICWizard Documentation
#########################

**MIMICWizard** is a Shiny app allowing user to navigate throught the PhysioNet MIMIC-IV database, a freely accessible deidentified electronic health record (EHR) dataset

Introduction
**************

The advent of Open-Access Electronic Health Records (EHRs) has revolutionized the landscape of clinical diagnosis and research. These digital versions of patient charts provide real-time, patient-centred records that provide precious information about patient state during its hospital stay.
However, the full potential of EHRs is yet to be realized due to two major constraints. 

First, access to patient databases is often restricted, limiting the scope of research and analysis. Second, there exists a significant technical barrier for non-technical users who wish to explore these databases but lack the necessary data science skills. 

Initially designed for medical practitioner, it offer a tool to help drawing and exploring new hypothesis. 

Getting started
***************

As MIMIC-IV database can be considered as open-source database, it's still under restricted access. User should follow a training about patient data management and sign an agreement to access the data.
That's why MIMICWizard is offering the possibilitiy to use demo database which contain only 100 patients but could showcase the app features.

**Requirements** 

* PostgreSQL Portable v15 (or greater)
* R version 4.2 (or greater)
* MIMIC-IV Clinical Database files `demo file <https://physionet.org/content/mimic-iv-demo/>`_ or request a `full access <https://mimic.mit.edu/docs/gettingstarted/>`_

.. note::

   MIMICWizard has been developped to work with a Postgres database. The application is not intented to be compatible with BigQuery or other proprietary solution

.. versionchanged:: 1.3
   Changed

Navigate through the app 
************************


Extended usage with data-science knowledge
******************************************


Changelog
*********


Research and development team
=============================

This application was originally developed by the Common Research Laboratory of Edouard Herriot Hospital (Laboratoire Commun de Recherche - HCL-bioMérieux, Lyon, France).

.. rst-class:: logo-container

|pic1| |pic2| |pic3|

   .. |pic1| image:: assets/Logo_LCR.png
      :height: 90px
      :alt: Hospices Civils de Lyon logo

   .. |pic2| image:: assets/LogoHCL.jpg
      :height: 90px
      :alt: Hospices Civils de Lyon logo

   .. |pic3| image:: assets/bm_logo_circle_rgb.png
      :height: 130px
      :alt: bioMérieux logo

The app is provided under open-source GNU GPLv3 licence. All contributions and suggestions are welcome. Learn more about contribution in our dedicated page How to contribute
*Read about the MIMICWizard research paper*

.. note::

   This project is under active development.


References and data
*******************


**Read about MIMIC-IV database and Physionet repository**


.. toctree::
   :maxdepth: 3
   :hidden:
   
   index
   gettingstarted