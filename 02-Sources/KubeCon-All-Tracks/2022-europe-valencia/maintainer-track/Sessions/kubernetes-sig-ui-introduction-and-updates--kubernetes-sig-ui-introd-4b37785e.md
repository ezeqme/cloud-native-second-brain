---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Sebastian Florek", "Marcin Maciaszczyk", "Kubermatic", "Shu Muto", "NEC"]
sched_url: https://kccnceu2022.sched.com/event/ytpx/kubernetes-sig-ui-introduction-and-updates-sebastian-florek-marcin-maciaszczyk-kubermatic-shu-muto-nec
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+SIG+UI+Introduction+and+Updates+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes SIG UI Introduction and Updates - Sebastian Florek & Marcin Maciaszczyk, Kubermatic; Shu Muto, NEC

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Sebastian Florek, Marcin Maciaszczyk, Kubermatic, Shu Muto, NEC
- Schedule: https://kccnceu2022.sched.com/event/ytpx/kubernetes-sig-ui-introduction-and-updates-sebastian-florek-marcin-maciaszczyk-kubermatic-shu-muto-nec
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+SIG+UI+Introduction+and+Updates+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes SIG UI Introduction and Updates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytpx/kubernetes-sig-ui-introduction-and-updates-sebastian-florek-marcin-maciaszczyk-kubermatic-shu-muto-nec
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+SIG+UI+Introduction+and+Updates+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3IC7_2Zj1fg
- YouTube title: Kubernetes SIG UI Introduction and Updates - Sebastian Florek & Marcin Maciaszczyk, Shu Muto
- Match score: 0.731
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-sig-ui-introduction-and-updates/3IC7_2Zj1fg.txt
- Transcript chars: 13309
- Keywords: dashboard, server, translation, support, metrics, container, architecture, cluster, browser, resources, connected, working, clusters, version, already, please, basically, updates

### Resumo baseado na transcript

today we will be giving you a short update from the kubernetes sig ui and also some introduction to the project uh i'm martin machastreck i work at kubernetes i'm sebastian florek and i also work at cobramatik unfortunately shumuto who is working at neg couldn't join us today but he's also one of the sigui chairs and he's part of the presentation is pre-recorded so we will play it and then we will continue with our part yes hello everyone i'm sure moto from nsc i was preparing as

### Excerpt da transcript

today we will be giving you a short update from the kubernetes sig ui and also some introduction to the project uh i'm martin machastreck i work at kubernetes i'm sebastian florek and i also work at cobramatik unfortunately shumuto who is working at neg couldn't join us today but he's also one of the sigui chairs and he's part of the presentation is pre-recorded so we will play it and then we will continue with our part yes hello everyone i'm sure moto from nsc i was preparing as much as i could to see you there i'm very sorry that i couldn't go to valencia after all so i'd like to talk the introduction section with video recording kubernetes dashboard is a general purpose webview based ui for kubernetes clusters it allows users to manage applications running in the cluster and troubleshoot them as well as manage the cluster itself this project is managed in a repository on github written here the lyrius is at the project's own timing and the current version is 2.5.1 that supports kubernetes to 1.23.6 we are aiming to support the latest version of kubernetes i've already created the approved for supporting kubernetes version 1.24 so maybe a new version of dashboard has been released already kubernetes dashboard is packaged in one binary but it consists of the front end and the backend also to get and to visualize the metrics of the cluster metallic server and dashboard metrics script needed the front end is written in typescript run in browser and it accesses the background to get information for your kubernetes cluster the bargain is leading go around learning your kubernetes cluster and this accesses tubernates api server using kubernetes go modules and metrics server via dashboard metrics scraper dashboard metrics scraper is also managed by cbui so please ask us about this but please ask sigue instrumentation about metrics server there are several ways to try out the dashboard the simplest way is to apply the manifest in the dashboard repository we also provide a helm chart which is also available external access to the dashboard is not allowed by default to prevent easy security instance so use cube control proxy or cube control portfolio to access dashboard this manifest has little authority by default so you need to add more permissions to show and operate various kubernetes resources you can use the sample user for the dashboard trial described in our documentation but this have a lot of authority so be careful when use it dashboard users should fam
