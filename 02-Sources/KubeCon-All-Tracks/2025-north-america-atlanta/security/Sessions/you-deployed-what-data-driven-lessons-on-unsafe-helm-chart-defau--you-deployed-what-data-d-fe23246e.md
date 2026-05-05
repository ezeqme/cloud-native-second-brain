---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["Security", "Storage Data"]
speakers: ["Yossi Weizman", "Microsoft"]
sched_url: https://kccncna2025.sched.com/event/27Fen/you-deployed-what-data-driven-lessons-on-unsafe-helm-chart-defaults-yossi-weizman-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=You+Deployed+What%3F%21+Data-Driven+Lessons+on+Unsafe+Helm+Chart+Defaults+CNCF+KubeCon+2025
slides: []
status: parsed
---

# You Deployed What?! Data-Driven Lessons on Unsafe Helm Chart Defaults - Yossi Weizman, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Storage Data]]
- País/cidade: United States / Atlanta
- Speakers: Yossi Weizman, Microsoft
- Schedule: https://kccncna2025.sched.com/event/27Fen/you-deployed-what-data-driven-lessons-on-unsafe-helm-chart-defaults-yossi-weizman-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=You+Deployed+What%3F%21+Data-Driven+Lessons+on+Unsafe+Helm+Chart+Defaults+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre You Deployed What?! Data-Driven Lessons on Unsafe Helm Chart Defaults.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fen/you-deployed-what-data-driven-lessons-on-unsafe-helm-chart-defaults-yossi-weizman-microsoft
- YouTube search: https://www.youtube.com/results?search_query=You+Deployed+What%3F%21+Data-Driven+Lessons+on+Unsafe+Helm+Chart+Defaults+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tssAofKij6g
- YouTube title: You Deployed What?! Data-Driven Lessons on Unsafe Helm Chart Defaults - Yossi Weizman, Microsoft
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/you-deployed-what-data-driven-lessons-on-unsafe-helm-chart-defaults/tssAofKij6g.txt
- Transcript chars: 23189
- Keywords: default, cluster, applications, misconfigurations, authentication, internet, exposed, identify, access, application, security, actually, balancer, deploy, containers, dashboard, configuration, clusters

### Resumo baseado na transcript

Unfortunately, Michael couldn't attend so I will represent both of us and this is the agenda for today. Then we will talk about um a real world incident that actually started our entire research. It was a serious it was a serious uh security risk and that's why in the later versions uh tiller was removed and helm was changed. Another example is the old Kubernetes dashboard which was a web interface to manage the cluster. example is couplow which is a very popular framework for building ML pipelines ML pipelines and kubernetes um and here also in the past installations of this framework didn't include built-in authentication and we saw quite many instances of coupe flow back then uh that were exposed to the internet without authentication and were quickly exploited including in a very large scale campaign that we observed.

### Excerpt da transcript

My name uh Yosi Wiseman. I'm a principal security researcher at Microsoft. Um Michael Kachinsky is my partner in this uh research. Unfortunately, Michael couldn't attend so I will represent both of us and this is the agenda for today. Um we will talk about default misconfigurations. Uh so we will start with an overview of default misconfigurations. Then we will talk about um a real world incident that actually started our entire research. Then we will talk about how did we identify misconfigurations in large scale by using scanner we developed. Uh then we will talk about containerized AI applications and we will share statistics and we will talk about how can we secure our environments from this uh type of risks. Okay. So let's start. So let's start by talking about misconfigurations. So in the past um many cloudnative applications weren't very secured by default and in general security wasn't always a first priority and let's see some examples that maybe some of you are familiar with. Uh so first the first the first example is Helm.

As many of you know, uh in its earlier versions, Helm came with a serverside component called Tiller. Uh this component had permissive clusterwide permissions in order to manage the deployments in the cluster. And Tiller didn't enforce authentication. So any pod in the cluster could talk to it. So if an attacker got even a limited access to the cluster, uh they could leverage tiller to get um full control. It was a serious it was a serious uh security risk and that's why in the later versions uh tiller was removed and helm was changed. Another example is the old Kubernetes dashboard which was a web interface to manage the cluster. Depends on the exact version. There were several um sometimes it came without authentication. Also in this case once you had initial access in the cluster you could use the dashboard for privilege escalation and in some cases users even exposed the dashboard to the internet uh which really helped to the attackers in those cases and the last example is couplow which is a very popular framework for building ML pipelines ML pipelines and kubernetes um and here also in the past installations of this framework didn't include built-in authentication and we saw quite many instances of coupe flow back then uh that were exposed to the internet without authentication and were quickly exploited including in a very large scale campaign that we observed.

And what's common to all of those applications uh was tha
