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
themes: ["AI ML", "Security", "GitOps Delivery", "Community Governance"]
speakers: ["Stefan Prodan", "Weaveworks"]
sched_url: https://kccnceu2022.sched.com/event/ytlV/flux-security-deep-dive-stefan-prodan-weaveworks
youtube_search_url: https://www.youtube.com/results?search_query=Flux+Security+Deep+Dive+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Flux Security Deep Dive - Stefan Prodan, Weaveworks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Stefan Prodan, Weaveworks
- Schedule: https://kccnceu2022.sched.com/event/ytlV/flux-security-deep-dive-stefan-prodan-weaveworks
- Busca YouTube: https://www.youtube.com/results?search_query=Flux+Security+Deep+Dive+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Flux Security Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytlV/flux-security-deep-dive-stefan-prodan-weaveworks
- YouTube search: https://www.youtube.com/results?search_query=Flux+Security+Deep+Dive+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MjxZcY6THdc
- YouTube title: Flux Security Deep Dive - Stefan Prodan, Weaveworks
- Match score: 0.728
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/flux-security-deep-dive/MjxZcY6THdc.txt
- Transcript chars: 31523
- Keywords: flux, cluster, github, everything, release, version, controllers, controller, security, sources, secrets, multi-tenancy, libraries, custom, resources, clusters, events, whatever

### Resumo baseado na transcript

so my name is bartek and i will be your moderator today we have stefan with us uh talking about flux and security i would like to remind you about code of conduct and that we should have mask unless you are speaking for drinking and i would like to say also that we have two seats there as well for two people let's go two people come on two people but probably there are groups of six so they cannot split okay we'll have some time hopefully for questions us they run their own tests and if they find problems they come back to us but in the last year we didn't had any issues we had a couple of issues at the beginning with uh with our vixes v6 due to the c libraries that we use and so on but those are sorted right so we all these tests are running using kubernetes kind and kubernetes kind is is a great way of running end-to-end tests because it it runs a whole cluster in a single container so you need a docker or something like that spin up a whole cluster and you can test on different kubernetes versions right and we support for example flux works from now 20 to 24. so we can test on all all the minor versions and make sure we didn't break something because the kubernetes api changes a lot uh and the client go changes a lot all the go libraries so we we really try to make everything possible

### Excerpt da transcript

so my name is bartek and i will be your moderator today we have stefan with us uh talking about flux and security i would like to remind you about code of conduct and that we should have mask unless you are speaking for drinking and i would like to say also that we have two seats there as well for two people let's go two people come on two people but probably there are groups of six so they cannot split okay we'll have some time hopefully for questions and if not uh there is definitely you know time afterwards where you can catch stefan or you can use slack channel or virtual hybrid platform meetings there is also a flux booth i will talk about it yeah probably you will be there all day with this in mind let's let's start all to you stephan thank you welcome everyone by the way [Music] [Applause] welcome everyone i'm very excited to be here two years of virtual conferences here wearing me down and i saw so nice to see everyone face to face so for those that don't know me i'm stefan prodan i work at weworks i'm a flux and flagger maintainer for five years now and i'm very happy to you know talk about you about flux and the security aspects of flux but first of all if you want this shirt please come by the flux booth you'll have to answer a short quiz and if you are here you'll definitely be able to answer it so don't be afraid of it it's really really easy come by and get our flex your flux t-shirt okay so a little introduction to the flux project so we have a organization called flag cd which is under cncf we are an incubation project we applied for graduation and this is going well so hopefully by next cubecon will be a graduated project the main projects in the in the flux organizations are flux 2 why is flux 2 because when we started flux nearly six years ago there was no you know there were no crds there was no operator idea inside kubernetes upstream so flux version one was a simple demand that you if you want to configure it you'll do that at install time if you want to reconfigure it you'll have to reinstall it in a way right so there was no dynamic configuration because we didn't have custom resources two years ago we started working on flux version two and we have uh split flux version one into uh flux originals like a monolith to do all things like talking to git applying things on the cluster and so on in version 2 this repo holds the cli and references to all the other flux components so flux is now joined a micro services idea where we have th
