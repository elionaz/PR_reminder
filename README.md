
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Open PR Slack Reminder</h3>

  <p align="center">
    This is a python bot that will help to your organization to make reminders if a PR is open for more than 24 hours
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



This project is for the next propose, key features
* Get Open PRs
* Not Drafts
* Send notification to the owner via slack



### Built With


 [![Python][Python.org]][Python-url]



<!-- GETTING STARTED -->
## Getting Started

This is a simple script

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Using Homebrew
  ```sh
  $(brew --prefix python)/libexec/bin
  ```
* Setuptools, pip, etc.
 ```sh
  python3 -m pip install --upgrade setuptools
  python3 -m pip install --upgrade pip
  ```
  
### Installation 

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a GitHub Token
2. Create an Slack App ([https://api.slack.com/apps](https://api.slack.com/apps))
3. Add to the app scope
   ```sh
   chat:write
   conversations.invite
   ```
4. Generate a token for the Slack Bot
5. Invite the bot to the selected channel
6. Modify the .env file with the tokens, org name, slack channel and channel id

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You need to install the dependencies before running the script.

   ```sh
 pip3 install requests
 pip3 install python-dotenv
 pip3 install python-dateutil
 pip3 install slack_sdk
 pip3 install --upgrade slack-sdk
   ```
Also you will need to modify the `usernames.py` file by changing the json to your actual dictionary where the first value is the github username and the second is the slack user id
  ```sh
  github_to_slack_usernames = {
     'elionaz': 'UXXXX',
     'elionaz0': 'UXXXX'
 }
   ```
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>







<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-FF2D20?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.co
[Docker-url]: https://www.docker.com/
[Docker.com]: https://img.shields.io/badge/-Docker-000000?&logo=Docker
[Typescriptlang-url]: https://www.typescriptlang.org/
[Typescriptlang.org]: https://img.shields.io/badge/-TypeScript-000000?&logo=TypeScript
[Spring-url]: https://spring.io/
[Spring.io]: https://img.shields.io/badge/Spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white
[Java-url]: https://www.java.com/
[Java.com]: https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white
[Kotlin-url]: https://kotlinlang.org/
[Kotlin.org]: https://img.shields.io/badge/Kotlin-0095D5?&style=for-the-badge&logo=kotlin&logoColor=white
[Swift-url]: https://www.apple.com/swift/
[Swift.com]: https://img.shields.io/badge/Swift-FA7343?style=for-the-badge&logo=swift&logoColor=white
[Python-url]: https://www.python.org/
[Python.org]: https://img.shields.io/badge/Python-yellow?style=for-the-badge&logo=Python&logoColor=white[Python.org]: https://img.shields.io/badge/Python-yellow?style=for-the-badge&logo=Python&logoColor=white
