---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security"]
speakers: []
sched_url: https://kccncna2023.sched.com/event/1VDni/security-hub-unconference-seccomp-policy-usage-why-there-is-no-adoption
youtube_search_url: https://www.youtube.com/results?search_query=SECURITY+HUB+UNCONFERENCE%3A+Seccomp+policy+usage%3A+why+there+is+no+adoption%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# SECURITY HUB UNCONFERENCE: Seccomp policy usage: why there is no adoption?

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Chicago
- Speakers: N/A
- Schedule: https://kccncna2023.sched.com/event/1VDni/security-hub-unconference-seccomp-policy-usage-why-there-is-no-adoption
- Busca YouTube: https://www.youtube.com/results?search_query=SECURITY+HUB+UNCONFERENCE%3A+Seccomp+policy+usage%3A+why+there+is+no+adoption%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre SECURITY HUB UNCONFERENCE: Seccomp policy usage: why there is no adoption?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1VDni/security-hub-unconference-seccomp-policy-usage-why-there-is-no-adoption
- YouTube search: https://www.youtube.com/results?search_query=SECURITY+HUB+UNCONFERENCE%3A+Seccomp+policy+usage%3A+why+there+is+no+adoption%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=O5_UF1-ineg
- YouTube title: SECURITY HUB UNCONFERENCE: Seccomp policy usage: why there is no adoption?
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/security-hub-unconference-seccomp-policy-usage-why-there-is-no-adoptio/O5_UF1-ineg.txt
- Transcript chars: 26337
- Keywords: default, container, profile, policy, application, actually, runtime, question, containers, profiles, answer, network, create, seccom, policies, gvisor, probably, docker

### Resumo baseado na transcript

good afternoon everybody so my name is Matias I'm working with Ben at armo which is a security startup specialized in communities uh scanning and hardening and yeah today we will talk about SE comp so I will I have like few points to introduce what it is and then we are really doing this un conference to get feedback from users whether you know it and if you know it if you use it and if not trying to understand if it makes sense to implement uh some capabilities

### Excerpt da transcript

good afternoon everybody so my name is Matias I'm working with Ben at armo which is a security startup specialized in communities uh scanning and hardening and yeah today we will talk about SE comp so I will I have like few points to introduce what it is and then we are really doing this un conference to get feedback from users whether you know it and if you know it if you use it and if not trying to understand if it makes sense to implement uh some capabilities into Cube scape or just if nobody cares so what is SE comp so SE comp is uh a feature of the Linux kernel since 2.6 something like this so very old and um it enables to block uh C SCS from the user space to the kernel space so you can also configure it to just uh create warnings but usually we want to block it so why is it good to use set comp well you can protect your canel from malicious apps because let's face it the Linux canel has like dozens of Cs and few of them are are used by everybody and then they are all those special management one that are never used and since they are never used they have issues and people can abuse them so usually it's a it's a good idea to restrict them and it's mostly harmless for most of the applications so who learned about setcom for the first time right now did everyone know about it before okay there are a few hands so that's that's good so somewhere we have done something good that people learned seccom for the first time today so that's great and uh it's been one of the main things in terms of isolation for containers uh so it's really important topic and uh I hope we can only from containers I mean usually it's for regular processes and and containers are special cases of processes uh so now if if I can Circle back to kubernetes so SE comp has been available since 119 which means more than 3 years ago it was August 2020 and we haven't seen that much of an adoption uh so usually what what you have available is like few built-in profiles that are available in communities like mostly the default one and uh you can or there is also the unrestricted one which is not profile and when you create your your pods uh yeah you can apply this these profiles to to the to to your application but the the default one is like way too General so what is good is usually to write your own profile but then you run into like problems of how do I take this configuration which is a Linux configuration into all my nodes how do I like synchronize and distribute these profiles and an
