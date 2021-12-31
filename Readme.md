
<!--
*** Thanks for checking out the README. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again!
-->

<!--
# ===========================================================================
#
# NAME: User Access Key Rotation every X number of Days.
# AUTHOR: Mohamad
# DATE  : 21/11/2021
#
# Refer: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/iam-example-managing-access-keys.html
#
# ===========================================================================
-->

<!-- ABOUT THE Code -->
## About The Code

Script to Check the User Access Key Age and Inactivate it once it reaches 80 Days, 
by triggering the script every day once by the CloudWatch Rule

Refer: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/iam-example-managing-access-keys.html

Here's how it works:
* We provide the Username to check the Access Key's Created Date
* Next, check the Age of the Access key since it was created.
* Next, if Access Key Age is 80 or more than 80 > "Inactive" the Key. If not reached 80 Days "No Action Taken"

Pending work:
Need to work on to delete the the access key instead of deactivating it.

<p align="right">(<a href="#top">back to top</a>)</p>
