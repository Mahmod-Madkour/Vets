# Vets Web App

## Table of Contents

## 1- Introduction

### It is a web application like Facebook and LinkedIn, but it is intended for veterinarians
### Where they can communicate with each other in their field of specialization through a web program that contains 4 features:

  > 1- Publish posts, comments, replies and likes.

  > 2- Exchanging questions and answers among themselves.

  > 3- The most important thing is to share the disease of the animal or bird and find a cure for this disease.

  > 4- A personal account for each doctor containing his name, photo, and identification


### Technologies
  - ### Frontend
     - **Html**
     - **CSS**
     - **JS**
     - **Bootstrap**
  - ### Back-End
     - **Python**
     - **Django Framwork**

> [!NOTE]
> Important information for understanding and operating the project


    |-- django_env
    |   |-- Include
    |   |-- Lib
    |   |-- Scripts
    |   |-- vets
    |   |   |-- account
    |   |   |   |-- migrations
    |   |   |   |-- templates
    |   |   |   |   |-- auth
    |   |   |   |   |-- disease
    |   |   |   |   |-- post
    |   |   |   |   |-- profile
    |   |   |   |   |-- question
    |   |   |   |-- __init__.py
    |   |   |   |-- admin.py
    |   |   |   |-- apps.py
    |   |   |   |-- forms.py
    |   |   |   |-- models.py
    |   |   |   |-- tests.py
    |   |   |   |-- urls.py
    |   |   |   |-- views.py
    |   |   |-- media
    |   |   |   |-- disease
    |   |   |   |-- profile
    |   |   |   |-- therapy
    |   |   |-- static
    |   |   |   |-- css
    |   |   |   |-- js
    |   |   |-- templates
    |   |   |   |-- base_auth.html
    |   |   |   |-- base.html
    |   |   |-- vets
    |   |   |   |-- __init__.py
    |   |   |   |-- asgi.py
    |   |   |   |-- settings.py
    |   |   |   |-- urls.py
    |   |   |   |-- wsgi.py
    |   |   |-- db.sqlite3
    |   |   |-- manage.py



> [!NOTE]
> Useful information that users should know, even when skimming content.
## 2- Features
  - ### Authentication
      - **Register**
          - **Enter your Username [Uniqe]**
          - **Enter your Email [Uniqe]**
          - **Enter your First Name**
          - **Enter your Last Name**
          - **Enter your Password**
          - **Enter Confirm Password**
      - **Login**
          - **Enter your Username**
          - **Enter your Password**
      - **Forget Password**
          - **Enter your Email**
          - **Send Msg To Your Email**
              - **Enter your New Password**
              - **Enter Confirm New Password**
              - **Go To Login**
      <p float="left">
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/38e71b23-e25e-4484-88fa-9d4a30af9e84" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/5b988f89-ed85-42b8-8fd3-775829d172a9" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/5dcc528e-4390-4330-a8fe-15c7c46f1e9c" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/944678db-90a2-4285-b6da-00a7b77320ca" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/3a3eda3b-37cd-44e0-80b0-0a31b6b6c8f8" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/1245f134-2442-4fff-b5db-f5881ec9eca0" />
      </p>
  - ----------
  - ### Posts
      - **Display All Posts**
      - **Create Post**
          - **Enter Body of Post**
      - **Update Your Post**
      - **Delete Your Post**
      - **Like and Dislike of Any Post**
      - :black_medium_small_square: :black_medium_small_square: :black_medium_small_square:
      - **Add Comment to Any Post**
          - **Enter Body of Comment**
      - **Update Your Comment**
      - **Delete Your Comment**
      - **Like and Dislike of Any Comment**
      - :black_medium_small_square: :black_medium_small_square: :black_medium_small_square:
      - **Add Replay to Any Comment**
          - **Enter Body of Replay**
      - **Update Your Replay**
      - **Delete Your Replay**
      - **Like and Dislike of Any Replay**
      <p float="left">
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/ec5a4874-b47e-46fb-96a2-5426cf4e62bc" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/5b4a3f87-b113-4afb-8cef-39b3e4c9298e" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/4f6a4b5f-20e7-426c-8998-6c6008e41e3c" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/e2d33eb3-a25a-427c-9301-2d78fadcf120" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/f1f987c5-d535-449f-9108-29026df893d3" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/1271f880-a7ec-4247-b402-76b6f9fa3017" />
      </p>

  - ----------
  - ### Questions
      - **Display All Questions**
      - **Display All Questions are Answered**
      - **Display All Questions are Not Answered**
      - :black_medium_small_square: :black_medium_small_square: :black_medium_small_square:
      - **Ask Question**
          - **Enter Title of Question [Uniqe]**
          - **Enter Body of Question**
          - **Status of Question is Not Answered by default**
      - **Delete Your Question**
      - **Update Status of your Question [*Answered*, *Not Answered*]**
      - **Vote and Disvote of Any Question**
      - :black_medium_small_square: :black_medium_small_square: :black_medium_small_square:
      - **Add Answer to Any Question**
      - **Delete Your Answer**
      - **Vote and Disvote of Any Answer**
      <p float="left">
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/2f4bbf39-dfd4-4c70-a0fe-faddb67fb767" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/f2e159bc-1000-443d-a379-4150a4973f5f" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/8b46f3d4-07c6-4f80-9992-1dc6a922c6eb" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/5f1a51c8-0119-47c7-b41a-ff5b96f8c8ae" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/cd41c51c-d3ca-46c8-9af9-7dc1f14c439d" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/d7e5d8ed-a2d7-45f8-bdaa-5c6953be2789" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/fbde941d-db3c-4840-930e-782add78e9e8" />
      </p>

  - ----------
  - ### Diseases
      - **Display All Diseases**
      - **Display All Diseases are Same Category**
          - **Fungal Disease**
          - **Protozoal Disease**
          - **Bacterial Disease**
          - **Parasitic Disease**
          - **Viral Disease**
      - :black_medium_small_square: :black_medium_small_square: :black_medium_small_square:
      - **Add Disease**
          - ***Enter Description of Disease***
          - ***Upload Photo for Disease***
          - ***Choose Category of Disease***
      - **Delete Your Disease**
      - :black_medium_small_square: :black_medium_small_square: :black_medium_small_square:
      - **Add Therapy to Any Disease**
          - ***Enter Description of Therapy***
          - ***Upload Photo for Therapy [optional]***
      - **Delete Your Therapy**
      <p float="left">
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/3bd26c0e-1586-4db1-90e1-46e9312a4293" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/0e623336-103e-45f8-81f4-a44f92f52c2e" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/5d328cf3-01e3-4cf9-8f7e-5ac8097ce11e" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/b8f06411-4ce7-4199-9fcb-9acf0dc0a1de" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/015491df-a6ed-42b1-adb9-b88682993c6a" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/7c1c8c9b-1d2b-45be-a004-8784bf061c2f" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/0984f6e8-068b-4c9a-ace0-1b98eb00528b" />
      </p>
      
  - ----------
  - ### Profile
      - **Show Your Profile**
          - **Show Your Name**
          - **Show Your Profile Picture**
          - **Show Your About**
      - **Update Profile**
          - **Update Your First Name**
          - **Update Your Last Name**
          - **Update Your First Name**
          - **Update Your About**
          - **Change Your Profile Picture**
      - **Change Your Password**
         - **Enter Old Password**
         - **Enter New Password**
         - **Enter Confirm New Password**
      <p float="left">
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/aac84136-28eb-4227-b4cb-56709980db0e" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/cb1e47a1-45ac-496c-be2a-4130720e4a02" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/d638564d-fdb4-4cfc-b460-f37588a47d79" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/f69c0d82-52c6-4091-996f-163f90785f5a" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/a514ae60-a9a6-4b72-bfff-d69dd24f6fd7" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/33455d5d-ece1-497b-aec8-5c40e1752e96" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/69ed2fa8-c407-48fe-b166-f330d9a7030f" />
        <img width="200" high="200" src="https://github.com/Mahmod-Madkour/vets/assets/80865998/ec2e6dfc-c298-4958-89a4-2ca5643c4701" />
      </p>

  - ----------
