---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Zhonghu Xu", "Huawei", "Nic Jackson", "Hashicorp"]
sched_url: https://kccnceu2025.sched.com/event/1td0t/cncf-tag-network-and-cloud-native-network-landscape-zhonghu-xu-huawei-nic-jackson-hashicorp
youtube_search_url: https://www.youtube.com/results?search_query=CNCF+TAG+Network+and+Cloud+Native+Network+Landscape+CNCF+KubeCon+2025
slides: []
status: parsed
---

# CNCF TAG Network and Cloud Native Network Landscape - Zhonghu Xu, Huawei & Nic Jackson, Hashicorp

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Zhonghu Xu, Huawei, Nic Jackson, Hashicorp
- Schedule: https://kccnceu2025.sched.com/event/1td0t/cncf-tag-network-and-cloud-native-network-landscape-zhonghu-xu-huawei-nic-jackson-hashicorp
- Busca YouTube: https://www.youtube.com/results?search_query=CNCF+TAG+Network+and+Cloud+Native+Network+Landscape+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre CNCF TAG Network and Cloud Native Network Landscape.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td0t/cncf-tag-network-and-cloud-native-network-landscape-zhonghu-xu-huawei-nic-jackson-hashicorp
- YouTube search: https://www.youtube.com/results?search_query=CNCF+TAG+Network+and+Cloud+Native+Network+Landscape+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gMDC1zzHabk
- YouTube title: CNCF TAG Network and Cloud Native Network Landscape - Zhonghu Xu, Huawei & Nic Jackson, Hashicorp
- Match score: 0.798
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/cncf-tag-network-and-cloud-native-network-landscape/gMDC1zzHabk.txt
- Transcript chars: 22122
- Keywords: network, projects, mesh, inside, sandbox, networking, looking, please, working, reboot, trying, application, semant, connect, groups, initiative, infrastructure, gateway

### Resumo baseado na transcript

I hope everybody's doing well and I hope you're not too exhausted being Friday, day five. Well, day five for me because I've been here since maintainer summit on Monday. So if you if you do run a kind of a regional setup on your Kubernetes clusters, coupube slice can actually help you to to route to a different cluster in the event that you you need that. So you start looking at like semant and k mesh and and what's going on here is you're getting a challenge on some of the traditional patterns that we would use in in service mesh. But then, you know, things like OVN, Kubernetes, we're looking at how the sort of the networking works. Um and and all of those, as I say, are kind of challenging the problems that we have today.

### Excerpt da transcript

Welcome. I hope everybody's doing well and I hope you're not too exhausted being Friday, day five. Well, day five for me because I've been here since maintainer summit on Monday. But welcome to the session and we we want to talk about the tag network and the the cloud native network landscape. Just as a kind of a quick preface, how many of you folks are aware of the the the network reboot or the the tag reboot that's happening inside of the CNCF at the moment? A few people are aware of what's going on. Okay. So, one one of the things about that is that tag network is going to get merged into tag infrastructure. We're going to dig into that in a little bit, but everything we're going to talk about is still relevant uh regardless of the fact that it might be tag infrastructure that you see at the next KubeCon. And with that, I'm going to hand up. Yeah, thank you, Nick. Uh my name is Jun Hushi. I'm from China, you know, an open source software engineer from Huawei. Yeah. And you okay uh today let's talk about uh the several parts.

Uh first one is what is tech t tech network? So it will be under the new tag framework. Yeah. But we want to uh let you know what we did last year. Yeah. And then the second part we will talk about the overview of tech network projects and we will cover several projects in the sense land scopes for the network scope. Yeah. Then we will uh talk about some works we did in the last 12 years uh sorry last 12 months. Yeah. And there are several projects in the last year that uh maybe evolve from the sandbox to incubation and also some new projects that on board uh sandbox. Then we have a quick demo for uh new project Kim mesh. Yeah. Then the last uh last two part we'll talk about uh how tech network will do after the tech reboot and then uh maybe uh before the new tech reboot is happen we want to let let all of us know how to participate in the network network work. Yeah. So what is a tech? Yeah. attack is a technical advisory group that is a long lived group that reports to the sync. Yeah. Uh the tech responsibilities is uh so many we can see see here it is to link the uh end users and the project contributors and also the TC members.

Yeah, we need to identify the gaps between the uh sens project and uh help them evolve to uh fill the gaps between the uh end user. Yeah. Then we also have to educate and inform users with unbiased effective and project uh practically useful information. Yeah. We need also need to focus on attention and
