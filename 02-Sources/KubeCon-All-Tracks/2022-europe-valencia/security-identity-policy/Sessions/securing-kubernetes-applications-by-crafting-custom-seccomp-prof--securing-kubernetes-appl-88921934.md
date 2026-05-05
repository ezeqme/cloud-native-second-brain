---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Security + Identity + Policy"
themes: ["Observability", "Security", "Kubernetes Core"]
speakers: ["Sascha Grunert", "Red Hat"]
sched_url: https://kccnceu2022.sched.com/event/ytml/securing-kubernetes-applications-by-crafting-custom-seccomp-profiles-sascha-grunert-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Securing+Kubernetes+Applications+by+Crafting+Custom+Seccomp+Profiles+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Securing Kubernetes Applications by Crafting Custom Seccomp Profiles - Sascha Grunert, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Observability]], [[Security]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Sascha Grunert, Red Hat
- Schedule: https://kccnceu2022.sched.com/event/ytml/securing-kubernetes-applications-by-crafting-custom-seccomp-profiles-sascha-grunert-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+Kubernetes+Applications+by+Crafting+Custom+Seccomp+Profiles+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Securing Kubernetes Applications by Crafting Custom Seccomp Profiles.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytml/securing-kubernetes-applications-by-crafting-custom-seccomp-profiles-sascha-grunert-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Securing+Kubernetes+Applications+by+Crafting+Custom+Seccomp+Profiles+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=alx38YdvvzA
- YouTube title: Securing Kubernetes Applications by Crafting Custom Seccomp Profiles - Sascha Grunert, Red Hat
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/securing-kubernetes-applications-by-crafting-custom-seccomp-profiles/alx38YdvvzA.txt
- Transcript chars: 26656
- Keywords: profiles, second, profile, default, application, security, container, recording, available, operator, itself, workload, process, recorder, syscall, create, automatically, actually

### Resumo baseado na transcript

hey everyone welcome to my talk about securing kubernetes applications by crafting custom second profiles i'm sasha and it's a pleasure to be here today what do we want to see in this talk so the first thing i would like to tell you about is a brief history about setcoming kubernetes so we reflect the development progress of second in kubernetes and we will see what the current state of second kubernetes is after that we will craft a customs account profile by hand for this we will use

### Excerpt da transcript

hey everyone welcome to my talk about securing kubernetes applications by crafting custom second profiles i'm sasha and it's a pleasure to be here today what do we want to see in this talk so the first thing i would like to tell you about is a brief history about setcoming kubernetes so we reflect the development progress of second in kubernetes and we will see what the current state of second kubernetes is after that we will craft a customs account profile by hand for this we will use a real world example and we will use two methods like tracing the logs and running recording second profiles by using ebpf after that we will speak about how we can automate away those manual efforts so how we how could it be possible to integrate our recording into a ci cd system for example and how we can get rid of all those manual steps in between and after that we will speak about the bright future of a per default more secure kubernetes so how can we make the kubernetes more secure by default by using second profiles for example second is a cisco interceptor feature for the linux kernel so it really works like this so you want to do a this call on your application and then you can decide which which action do you want to take with this syscall so for example you have a different list of actions available you can for example say that you will only want to lock this action you want to arrow out or you want to allow this cisco for example and this can boost the application security by limiting the list of allowed syscalls so you can maintain a list of allowed cisco's you can also maintain a list of blocked syscalls and you can also find greatly define what the error code for example should be in case your disallows this call and this has been added to kubernetes a long time ago so we also have a default security profile this has been defined by the container runtimes but kubernetes requires that such a profile exist in every container on time like container d cryo and docker second was going to ga which means generally available since kubernetes 1.90 so we now can consider this feature as stable since quite some releases and it also supports most linux kernel versions there are some constraints or there are some environments where second may be not supported so we also have to take this into consideration that we have for example a decent architecture or linux distribution it does not support secop at all but in general this second fields are usable by a dative field in t
