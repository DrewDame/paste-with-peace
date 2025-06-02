<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO
<br />
<div align="center">
  <a href="https://github.com/DrewDame/paste-with-peace">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

![alt text](Animationv3.gif)

<h3 align="center">Paste With Peace</h3>

  <p align="center">
    Paste With Peace is a lightweight desktop app that helps prevent credential leaks before they happen. It watches your clipboard for things like API keys from providers like AWS and OpenAI, and if you try to paste something sensitive into Slack, it can automatically delete it or block the message from being sent. I built it in Python with a focus on the overlap between software engineering and security, and it was fun figuring out how to hook into things like clipboard monitoring, UI settings, and keypress detection in a way that's actually useful for everyday developers.
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Paste With Peace is a lightweight desktop app that helps prevent credential leaks before they happen. It watches your clipboard for things like API keys from providers like AWS and OpenAI, and if you try to paste something sensitive into Slack, it can automatically delete it or block the message from being sent. I built it in Python with a focus on the overlap between software engineering and security, and it was fun figuring out how to hook into things like clipboard monitoring, UI settings, and keypress detection in a way that's actually useful for everyday developers.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

- [Python](https://python.org)
- [Pytest](https://docs.pytest.org)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [PyWin32](https://github.com/mhammond/pywin32)
- And more, as explained in the <a href="#acknowledgments">Acknowledgements Section</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To run the credential scanner on Windows, simply download this repo, navigate to the "dist" folder, and run PasteWithPeace.exe in the command line with ./PasteWithPeace.exe or navigate through your file explorer and open the file. Comprehensive video guide has been attached below.

### Prerequisites

All Python dependencies are managed with pip and stored in requirements files:

- [`requirements.txt`](requirements.txt) contains all runtime (end-user) dependencies.
- [`requirements-dev.txt`](requirements-dev.txt) contains all developer dependencies (including test and build tools).

You need Python 3.9+ installed. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repo:
   ```sh
   git clone https://github.com/DrewDame/paste-with-peace.git
   cd paste-with-peace
   ```
2. Install runtime requirements (for end users):
   ```sh
   pip install -r requirements.txt
   ```
   If you are developing, contributing, or running tests, install all dev requirements:
   ```sh
   pip install -r requirements-dev.txt
   ```

3. To run the app, use:
   ```sh
   python main.py
   ```
   Or run the packaged executable from the `dist` folder if available.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The video below provides a comprehensive walkthrough of all features and usage scenarios for Paste With Peace. Watch it to see the app in action and learn how to get the most out of its capabilities.

<video controls src="PasteWithPeaceExplanation.mp4" title="Paste With Peace Feature Walkthrough"></video>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

For a detailed record of all past changes made to the project, please see the [change_log.txt](change_log.txt) file in the repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Drew Dame - drewdame@umich.edu

Project Link: [https://github.com/DrewDame/paste-with-peace](https://github.com/DrewDame/paste-with-peace)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This project uses the excellent [Best-README-Template](https://github.com/othneildrew/Best-README-Template/tree/main) as the foundation for its README structure.

This project was built with the help of many python libraries and frameworks that can be found by name in the [`requirements-dev.txt`](requirements-dev.txt) and [`requirements.txt`](requirements.txt) files.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/DrewDame/paste-with-peace.svg?style=for-the-badge
[contributors-url]: https://github.com/DrewDame/paste-with-peace/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DrewDame/paste-with-peace.svg?style=for-the-badge
[forks-url]: https://github.com/DrewDame/paste-with-peace/network/members
[stars-shield]: https://img.shields.io/github/stars/DrewDame/paste-with-peace.svg?style=for-the-badge
[stars-url]: https://github.com/DrewDame/paste-with-peace/stargazers
[issues-shield]: https://img.shields.io/github/issues/DrewDame/paste-with-peace.svg?style=for-the-badge
[issues-url]: https://github.com/DrewDame/paste-with-peace/issues
[license-shield]: https://img.shields.io/github/license/DrewDame/paste-with-peace.svg?style=for-the-badge
[license-url]: https://github.com/DrewDame/paste-with-peace/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/drewj-dame
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
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Python]: https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/150px-Python-logo-notext.svg.png
[Python-url]: https://python.org
[Pytest]: https://miro.medium.com/v2/resize:fit:800/1*F2BHs6p9erpiGKro5Pg1uQ.png
[Pytest-url]: https://docs.pytest.org
[PyAutoGUI]: https://
[Pyautogui-url]: https://pyautogui.readthedocs.io/en/latest/