---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Jeremy Rickard", "Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d4x/project-lightning-talk-copacetic-directly-patch-container-image-vulnerabilities-jeremy-rickard-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Copacetic%3A+Directly+Patch+Container+Image+Vulnerabilities+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Copacetic: Directly Patch Container Image Vulnerabilities - Jeremy Rickard, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Jeremy Rickard, Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d4x/project-lightning-talk-copacetic-directly-patch-container-image-vulnerabilities-jeremy-rickard-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Copacetic%3A+Directly+Patch+Container+Image+Vulnerabilities+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Copacetic: Directly Patch Container Image Vulnerabilities.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d4x/project-lightning-talk-copacetic-directly-patch-container-image-vulnerabilities-jeremy-rickard-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Copacetic%3A+Directly+Patch+Container+Image+Vulnerabilities+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gp2DVPBkECI
- YouTube title: Project Lightning Talk: Copacetic: Directly Patch Container Image Vulnerabilities - Jeremy Rickard
- Match score: 0.993
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-copacetic-directly-patch-container-image-vulner/gp2DVPBkECI.txt
- Transcript chars: 5153
- Keywords: container, docker, vulnerabilities, default, inside, images, report, directly, replace, installed, application, openssl, running, actually, features, instead, github, lightning

### Resumo baseado na transcript

Uh we're going to talk to you a little bit about what the project is and uh maybe get some interest for you. So, Copathetic is a project in the CNCF sandbox uh that is intended to directly patch images uh to to alleviate container vulnerabilities. Um before you had to essentially run it on whatever target architecture you were looking for.

### Excerpt da transcript

All right. Hey everybody, welcome uh to the lightning talks today. Hope you're finding some useful information. Um my name is Jeremy. I work at Microsoft on the Copaetic project. Uh we're going to talk to you a little bit about what the project is and uh maybe get some interest for you. So just as a quick show of hands, who hates CVE in container images? All right. So, Copathetic is a project in the CNCF sandbox uh that is intended to directly patch images uh to to alleviate container vulnerabilities. Um it's a CLI that's written in Go and it's based off of BuildKit which is the default builder for Docker. So, if you're using a newer version of Docker and you say Docker build, in essence, that's using Buildkit behind the scenes. There's a whole bunch of uh libraries that come along with that that help you to assemble um do operations on top of container images and uh Copa uses this to help us replace things in the container and generate a new container image without having to go through the full build process again.

And it does this by taking in a container vulnerability scan report. By default, it takes in Trivy. Um Trivy is an uh another popular project in the ecosystem. uh and by default it will take in the trivia report and look for the OS vulnerabilities. So uh things like maybe you have curl installed in the application in your container image or something like OpenSSL. Uh those are things that commonly get CVES and might show up in a scan. Uh TR uh Copa will take that scan and identify which uh things are vulnerable and then build off of there. That component is pluggable so you can replace it with another tool of your choice. uh but by default it uses trimming. And how this works is you take your base image. So we can call this the mcguffin image. Uh it's got an application layer, a frame framework layer, um maybe some other layers that have all the OS vulnerabilities or sorry OS packages installed inside of them. It's run through a tool like Trivy. That report is then passed into Copa, the CLI. You run it by running Copa with the the arguments.

It analyzes that uh that scan report and then it looks through the container image, determines what things need to be updated and then it generates a patch layer which is really just a diff between the things that were installed and the image that was there before and it generates a brand new layer that gets appended on top of the image. So you're able to take upstream things that you maybe don't build yo
