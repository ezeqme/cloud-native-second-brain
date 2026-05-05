---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Security + Identity + Policy"
themes: ["Security"]
speakers: ["Barun Acharya", "Accuknox"]
sched_url: https://kccncna2022.sched.com/event/182Ji/armoring-cloud-native-workloads-with-lsm-superpowers-barun-acharya-accuknox
youtube_search_url: https://www.youtube.com/results?search_query=Armoring+Cloud+Native+Workloads+With+LSM+Superpowers+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Armoring Cloud Native Workloads With LSM Superpowers - Barun Acharya, Accuknox

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: United States / Detroit
- Speakers: Barun Acharya, Accuknox
- Schedule: https://kccncna2022.sched.com/event/182Ji/armoring-cloud-native-workloads-with-lsm-superpowers-barun-acharya-accuknox
- Busca YouTube: https://www.youtube.com/results?search_query=Armoring+Cloud+Native+Workloads+With+LSM+Superpowers+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Armoring Cloud Native Workloads With LSM Superpowers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ji/armoring-cloud-native-workloads-with-lsm-superpowers-barun-acharya-accuknox
- YouTube search: https://www.youtube.com/results?search_query=Armoring+Cloud+Native+Workloads+With+LSM+Superpowers+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8jXuBelV3-0
- YouTube title: Armoring Cloud Native Workloads With LSM Superpowers - Barun Acharya, Accuknox
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/armoring-cloud-native-workloads-with-lsm-superpowers/8jXuBelV3-0.txt
- Transcript chars: 13912
- Keywords: access, container, containers, security, policy, control, account, malicious, inside, network, runtime, wordpress, kernel, enforcement, application, context, entities, activity

### Resumo baseado na transcript

hello everyone thank you for joining me on my session on armoring cloud native workloads with LSM superpowers I am varunachada I am a software engineering intern at equinox working on open source Cloud Security Solutions with the various advantages that containers provide organizations worldwide are rapidly adopting containers in one form or another we have applications running in containers across nodes across clusters with the rise of adoption of modern Cloud native infrastructure so has reserved the cyber attacks on the same containers are not really protected by default

### Excerpt da transcript

hello everyone thank you for joining me on my session on armoring cloud native workloads with LSM superpowers I am varunachada I am a software engineering intern at equinox working on open source Cloud Security Solutions with the various advantages that containers provide organizations worldwide are rapidly adopting containers in one form or another we have applications running in containers across nodes across clusters with the rise of adoption of modern Cloud native infrastructure so has reserved the cyber attacks on the same containers are not really protected by default as the various tools for security into place provides perimeter security at the host or the network and not necessarily the workload itself we have security focused node images hardened kernels strict configuration but there's a need to enforce security at container level hence the need for container security we usually have some static analyzers in place but they only let us know about what known vulnerabilities are containers are vulnerable to but recent vulnerabilities like log 4J and pawn kit could not have been detected statically that's like zero days malware meant to evade analyzers and privileges escalation attempts manifest at runtime and cannot be detected statically so how do we deal with vulnerabilities that manifest at runtime we deal with them at runtime so container runtime security we actively monitor what's happening with our containers at runtime and try to detect for the malicious in depth but how do we go about this to better understand let's go through an analogy let's imagine containers as a private apartment a private apartment with John and Jane each having their own rooms they have a kitchen and some maintenance staff around John and Jane value their privacy Jane doesn't like if Jon pokes into her room neither does John if Jane does the same but they both do like to hang around in the kitchen for functioning they generally don't want the maintenance staff to roam around in the apartment but in case something breaks like the shower is broken the gas is not working or some electrical Appliance is malfunctioning they need the maintenance staff around let's take this analogy back to Containers we have now a WordPress app a MySQL app they each have their own configurations and directory they need shared libraries to function and then we have cat and PS and other maintenance binaries that help us around in case something is broken but like I mentioned Apache WordPress
