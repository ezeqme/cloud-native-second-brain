---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Kubernetes Core"]
speakers: ["Jan Stomphorst", "ACC ICT"]
sched_url: https://kccnceu2026.sched.com/event/2EG0A/cloud-native-theater-cloud-native-university-kubernetes-and-the-answer-is-42-jan-stomphorst-acc-ict
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+Kubernetes+and+the+Answer+is%E2%80%A6+42%21+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Cloud Native University: Kubernetes and the Answer is… 42! - Jan Stomphorst, ACC ICT

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jan Stomphorst, ACC ICT
- Schedule: https://kccnceu2026.sched.com/event/2EG0A/cloud-native-theater-cloud-native-university-kubernetes-and-the-answer-is-42-jan-stomphorst-acc-ict
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+Kubernetes+and+the+Answer+is%E2%80%A6+42%21+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Cloud Native University: Kubernetes and the Answer is… 42!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG0A/cloud-native-theater-cloud-native-university-kubernetes-and-the-answer-is-42-jan-stomphorst-acc-ict
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+Kubernetes+and+the+Answer+is%E2%80%A6+42%21+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=U_7Reuwa3Uw
- YouTube title: Cloud Native Theater | Cloud Native University: Kubernetes and the Answer is… 42! - Jan Stomphorst
- Match score: 0.99
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-cloud-native-university-kubernetes-and-the-answer/U_7Reuwa3Uw.txt
- Transcript chars: 9752
- Keywords: application, container, running, configured, layers, deployment, network, limits, properly, nobody, memory, secret, applications, production, defined, containers, annotations, policies

### Resumo baseado na transcript

I'm a solutions architect working for as we're a Dutch company and we're specialist in cloudnative solutions. A first thing you have to do if you run it on Kubernetes is your application stateful or stateless you have to think about that foremost I want to do it stateless of course but you've got stateful applications so um yeah think about stateful A a a big problem if you use latest is your application uh is running as nonroot. You don't have to do that because uh the what Kubernetes does for you, it sets the limits. Are your uh Kubernetes default uh tolerations uh are sufficient or do you need different ones? Sometimes you have to think about uh running an application in Kubernetes.

### Excerpt da transcript

25 minutes so it's going to be fast and and loud. No. Um I'm Yan Stoneport. I'm a solutions architect working for as we're a Dutch company and we're specialist in cloudnative solutions. So what I wanted to talk about you've got your ultimate application. You're building your application and you want to run it on Kubernetes. And what do you have to do then to run that on Kubernetes? I've got 40 things to think about. So that's why I'm doing this checklist. Sorry, it's going to be a bit fast. It's So the first thing you have to do, yeah, we're skipping this. A first thing you have to do if you run it on Kubernetes is your application stateful or stateless you have to think about that foremost I want to do it stateless of course but you've got stateful applications so um yeah think about stateful stateless so do you have oh that's this is better do you have uh an sbomb generated for the application. Think about security. Um, you can use um Swift Triffy. Everybody know the Triffy hack that happened two days ago.

Read read the news. It's it's really a a thing. So, um, does your application run as, uh, pit one and does it handle a sick term properly? Because Kubernetes will kill your container. It will happen. Oh, by the way, don't use supervisor. Is anybody using supervised? Nobody. Thank you. Oh. Oh, no. So, is your application set to nonroot? Do you run your application as a as as a user? That's really important like WW data for an Apache machine. Is your image minimal like an Alpine or a DROless application? Smaller is better. And you can use Kubernetes debug for debugging your application if you want that. Are you removing unnecessary layers in your application? Layers are great. Um, you're using your layers for faster development. And if you have a lot of layers, the devel the the build times are going to be much slower. And if you have no layers, it's going to be really slow to build your application. So have enough layers, not too much. Are you using multi-stage deployments? Who's using multi-stage deployments? Everybody, hopefully.

Yeah, good. So, you don't want to have your uh um builder in your production image. That's Yeah, it's a a bigger attack factor. Is your image scanned by Trivy of course which has some vulnerabilities but is your is your image scanned before it goes to production and also scanned in production. Is your entry point um or command um properly um defined? cuz you've got your entry point and your command is overriding that. Who's
