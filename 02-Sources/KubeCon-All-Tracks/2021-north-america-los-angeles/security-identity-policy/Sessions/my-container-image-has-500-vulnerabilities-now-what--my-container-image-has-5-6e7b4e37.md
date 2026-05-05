---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Security + Identity + Policy"
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Matt Jarvis", "Snyk"]
sched_url: https://kccncna2021.sched.com/event/lV1T/my-container-image-has-500-vulnerabilities-now-what-matt-jarvis-snyk
youtube_search_url: https://www.youtube.com/results?search_query=My+Container+Image+has+500+Vulnerabilities%2C+Now+What%3F+CNCF+KubeCon+2021
slides: []
status: parsed
---

# My Container Image has 500 Vulnerabilities, Now What? - Matt Jarvis, Snyk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: United States / Los Angeles
- Speakers: Matt Jarvis, Snyk
- Schedule: https://kccncna2021.sched.com/event/lV1T/my-container-image-has-500-vulnerabilities-now-what-matt-jarvis-snyk
- Busca YouTube: https://www.youtube.com/results?search_query=My+Container+Image+has+500+Vulnerabilities%2C+Now+What%3F+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre My Container Image has 500 Vulnerabilities, Now What?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1T/my-container-image-has-500-vulnerabilities-now-what-matt-jarvis-snyk
- YouTube search: https://www.youtube.com/results?search_query=My+Container+Image+has+500+Vulnerabilities%2C+Now+What%3F+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1fO_xSnwDPg
- YouTube title: My Container Image has 500 Vulnerabilities, Now What? - Matt Jarvis, Snyk
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/my-container-image-has-500-vulnerabilities-now-what/1fO_xSnwDPg.txt
- Transcript chars: 21250
- Keywords: vulnerabilities, images, application, upstream, software, vulnerability, middleware, specific, container, security, dependencies, containers, process, docker, perhaps, strategy, issues, applications

### Resumo baseado na transcript

hi folks so this is me i'm matt jarvis i'm director of developer relations at sneak and snake are a cloud native application security company so when you first start scanning your container images um it can be a bit disconcerting to discover that you might have large numbers of vulnerabilities in your images um this is a scan i did last week on a vulnerable node image that i built it's a fairly extreme example but you can see that this image out of the box is showing us

### Excerpt da transcript

hi folks so this is me i'm matt jarvis i'm director of developer relations at sneak and snake are a cloud native application security company so when you first start scanning your container images um it can be a bit disconcerting to discover that you might have large numbers of vulnerabilities in your images um this is a scan i did last week on a vulnerable node image that i built it's a fairly extreme example but you can see that this image out of the box is showing us having over 800 vulnerabilities in it so faced with this a lot of us will just freeze like a rabbit in headlights um when we get presented with this big list of cves common vulnerabilities and exposures um particularly if our focus is on application development and not system administration and what are we supposed to do with this information uh where do we start um i just wanted an image to run my node application in and already i'm facing this gigantic task to make it secure well the most important thing we need to remember is that fixing these things in containers isn't like fixing them in virtual machines or in real servers we don't want to get into upgrading individual packages and starting to manage the whole system we need to understand where vulnerabilities have got into our images before we can start thinking about what strategies we might use to remediate them to fix them and what we don't want to do is to have to read through every cve understand its impact understand how you might exploit it or to become too versed in the kind of dark arts of system administration we're going to look for solutions which align with the paradigms of containers so we want repeatability uh we want efficiency and as much as possible we want to stick with the ideas of immutability that come along with how we use containers so the first thing that's worth understanding in this context is how the images we're using might be constructed our container images are constructed in layers and those layers are coming from different places some of them we're creating in our own dockerfiles and some of them are being brought in as part of our build process it's likely we started from a base image in our docker file and then we added some of our own things during the build process perhaps we made some configuration changes for our environment and then we added some custom software um depending on how we construct our dockerfile we'll end up with these things uh separated into file system layers in our container im
