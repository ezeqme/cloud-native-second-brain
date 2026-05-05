---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Frank Gu", "Voiceflow"]
sched_url: https://kccncna2023.sched.com/event/1R2sd/how-we-optimized-our-developer-experience-with-telepresence-frank-gu-voiceflow
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Optimized+Our+Developer+Experience+with+Telepresence+CNCF+KubeCon+2023
slides: []
status: parsed
---

# How We Optimized Our Developer Experience with Telepresence - Frank Gu, Voiceflow

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Chicago
- Speakers: Frank Gu, Voiceflow
- Schedule: https://kccncna2023.sched.com/event/1R2sd/how-we-optimized-our-developer-experience-with-telepresence-frank-gu-voiceflow
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Optimized+Our+Developer+Experience+with+Telepresence+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre How We Optimized Our Developer Experience with Telepresence.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2sd/how-we-optimized-our-developer-experience-with-telepresence-frank-gu-voiceflow
- YouTube search: https://www.youtube.com/results?search_query=How+We+Optimized+Our+Developer+Experience+with+Telepresence+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KaJYMz3tlIo
- YouTube title: How We Optimized Our Developer Experience with Telepresence - Frank Gu, Voiceflow
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/how-we-optimized-our-developer-experience-with-telepresence/KaJYMz3tlIo.txt
- Transcript chars: 31080
- Keywords: telepresence, running, traffic, environment, cluster, computer, intercept, container, machine, billing, command, application, variables, gateway, converter, developer, thanks, deploy

### Resumo baseado na transcript

all right hello everyone thanks for coming uh before I begin did anyone lose a large roll of money wrapped in a rubber band cuz I found the rubber band terrible joke as bad as the first time Dr Octavius told it anyways this talk is about how we optimize developer productivity with telepresence some black magic made by folks are there at Ambassador Labs my name is Frank goo so first of all a little bit about myself I have about 10 years of full stack experience by full is exposed in a world accessible Ingress so if you want start hitting this address uh in this demo you'll be able to see the changes that I'm I'll be making live so for the initial deployment we have an app container with a config telepresence Command telepresence connect and what this command does is it establishes a connection between my computer here to the kubernetes cluster that I have running on eks and voila you can see this context has been connected successfully at this point if I go by just simply running telepresence connect so let's do something a little bit more interesting here I'll demonstrate how to generate an intercept and begin to run a debug workflow on my local computer so the command you want to run is tell telepresence intercept and the billing Gateway is the deployment any workloads whether it's demon sets replica sets or deployments work in this case in the Nam space cucon 2023 I'm...

### Excerpt da transcript

all right hello everyone thanks for coming uh before I begin did anyone lose a large roll of money wrapped in a rubber band cuz I found the rubber band terrible joke as bad as the first time Dr Octavius told it anyways this talk is about how we optimize developer productivity with telepresence some black magic made by folks are there at Ambassador Labs my name is Frank goo so first of all a little bit about myself I have about 10 years of full stack experience by full stack I started from the printed circuit boards as an electrical engineer worked my way through up the stack with embedded systems networking etc etc software development and finally I made my way to the cloud and that's where I found my calling today I worked in Engineering Management and I run a team fun fact about myself I'm a licensed pilot and my role today is the director of engineering at voice flow we are a post series a startup that specializes in building an IDE for building chat Bots involving gen technology as a startup one of the key characteristics is that I have to play many roles so I'm also a hack collector I've played software developer devops business relations as well as various fundraising activities and helping out with marketing but the one area that interests me the most is the one related to developer productivity any improvements we make in developer productivity will have multiplicative effects on the efficacy of my team so naturally this topic interests me greatly how can I augment the productivity of our team who is this talk for well this talk is mainly for people who just interact with kubernetes and want to develop with very fast iteration Cycles I won't get into super deep Tech but if you want more details about what telepresence looks like under the hood feel free to ping me after the presentation more than happy to discuss and Dive Right In the agenda today we first go over what the problem that haunts voice flow and some of the dev Community around kubernetes is some of the potential solutions that we've tried and figured out painfully that it didn't work what is telepresence and how do you tele APR presence into kubernetes and there will be a live demo where I can showcase how this would work in practice and finally I'll go over some key considerations in deploying this technology into your workloads so let's start off with the container workflow traditionally we just code build reload make sure it works hello world things work great to commit it and that'
