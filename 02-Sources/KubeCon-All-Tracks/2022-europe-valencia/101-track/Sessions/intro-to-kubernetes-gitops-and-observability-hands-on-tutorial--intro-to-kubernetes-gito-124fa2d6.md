---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "101 Track"
themes: ["Observability", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Joaquin Rodriguez", "Microsoft", "Tiffany Wang", "Weaveworks"]
sched_url: https://kccnceu2022.sched.com/event/ytkj/intro-to-kubernetes-gitops-and-observability-hands-on-tutorial-joaquin-rodriguez-microsoft-tiffany-wang-weaveworks
youtube_search_url: https://www.youtube.com/results?search_query=Intro+to+Kubernetes%2C+GitOps%2C+and+Observability+Hands-On+Tutorial+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Intro to Kubernetes, GitOps, and Observability Hands-On Tutorial - Joaquin Rodriguez, Microsoft & Tiffany Wang, Weaveworks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[101 Track]]
- Temas: [[Observability]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Joaquin Rodriguez, Microsoft, Tiffany Wang, Weaveworks
- Schedule: https://kccnceu2022.sched.com/event/ytkj/intro-to-kubernetes-gitops-and-observability-hands-on-tutorial-joaquin-rodriguez-microsoft-tiffany-wang-weaveworks
- Busca YouTube: https://www.youtube.com/results?search_query=Intro+to+Kubernetes%2C+GitOps%2C+and+Observability+Hands-On+Tutorial+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Intro to Kubernetes, GitOps, and Observability Hands-On Tutorial.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytkj/intro-to-kubernetes-gitops-and-observability-hands-on-tutorial-joaquin-rodriguez-microsoft-tiffany-wang-weaveworks
- YouTube search: https://www.youtube.com/results?search_query=Intro+to+Kubernetes%2C+GitOps%2C+and+Observability+Hands-On+Tutorial+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WKvogzTg2iM
- YouTube title: Intro to Kubernetes, GitOps, and Observability Hands-On Tutorial - Joaquin Rodriguez & Tiffany Wang
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/intro-to-kubernetes-gitops-and-observability-hands-on-tutorial/WKvogzTg2iM.txt
- Transcript chars: 54206
- Keywords: flux, resources, deployment, application, cluster, repository, customization, observability, allows, running, within, prometheus, little, namespace, created, source, create, grafana

### Resumo baseado na transcript

so hi everybody thank you so much for joining us today and many thanks to kubecon and cloudnativecon for having us we're really excited to be here in our session today we're going to be covering an introduction to kubernetes git ops and observability we're going to start out with a few introductory slides before moving on to the hands-on tutorial portion of our session today i'd like to kindly ask you to ask questions in chat and we will be having a dedicated q a session following the workshop um for this case right now we're just connecting to prometheus but i just wanted to show you that you have the capability of connecting to so many things you can connect to elasticsearch you know grafana temple azure monitor is there grafana cloud et cetera so there's so many options so many so many things out there there's so many plugins out there that you can use uh for today's demo we're just focusing on prometheus but i just wanted to like i said mention that this exists right and you can play with it should you choose to so okay so we have a prometheus data source uh it's pointed to our prometheus service if i click on save and test we know that everything is connected as expected and now if i

### Excerpt da transcript

so hi everybody thank you so much for joining us today and many thanks to kubecon and cloudnativecon for having us we're really excited to be here in our session today we're going to be covering an introduction to kubernetes git ops and observability we're going to start out with a few introductory slides before moving on to the hands-on tutorial portion of our session today i'd like to kindly ask you to ask questions in chat and we will be having a dedicated q a session following the workshop and to get us started i'd like to invite joaquin to introduce himself briefly hey everybody my name is joaquin rodriguez i work for microsoft under commercial software engineering i um i guess help customers uh with kubernetes and open source uh happy to be here i'm based in austin texas um yeah again thanks for having us and i'm tiffany wang i'm a solutions architect on the customer success team at weaveworks and i'm originally from southern california and i'm now based in london and like joaquin i work with customers to streamline delivery and deployment to kubernetes clusters both on premise and in public cloud following get ops so before we continue on with the introductory slides i'd like to invite you all to register for the hands-on section of our session today if you could please navigate to https cube101.dev the username and password are displayed on the screen and hopefully might be available somewhere in chat but if it's helpful the username is cube and the password is capital v at symbol valencia 22 exclamation point and um once you've conducted the basic auth to the registration page you'll need to register with your github username once you've registered you should check your email for a email invitation to the kubernetes 101 github org we'll be using the kubecon 2022 repository for our github code spaces which is where we're going to be conducting the workshop today so take a minute to take note of the username and password and i will be moving on from the slide but we have a wonderful moderator that hopefully you got the username and password awesome great so while i give you a few minutes to do that i'll begin with an introduction to kubernetes since you're all here at cubecon this is information that you probably already know but we can start from the very beginning and talk about how kubernetes is an open source cloud native computing foundation project for container orchestration it was initially created at google and now it is maintained by cncf
