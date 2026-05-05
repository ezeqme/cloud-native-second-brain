---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security", "Networking"]
speakers: ["Raymond de Jong", "Isovalent"]
sched_url: https://kccnceu2023.sched.com/event/1HyYr/adopting-network-policies-in-highly-secure-environments-raymond-de-jong-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Adopting+Network+Policies+in+Highly+Secure+Environments+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Adopting Network Policies in Highly Secure Environments - Raymond de Jong, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]], [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Raymond de Jong, Isovalent
- Schedule: https://kccnceu2023.sched.com/event/1HyYr/adopting-network-policies-in-highly-secure-environments-raymond-de-jong-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Adopting+Network+Policies+in+Highly+Secure+Environments+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Adopting Network Policies in Highly Secure Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYr/adopting-network-policies-in-highly-secure-environments-raymond-de-jong-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Adopting+Network+Policies+in+Highly+Secure+Environments+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yikVhGM2ye8
- YouTube title: Adopting Network Policies in Highly Secure Environments - Raymond de Jong, Isovalent
- Match score: 0.889
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/adopting-network-policies-in-highly-secure-environments/yikVhGM2ye8.txt
- Transcript chars: 26510
- Keywords: network, policies, namespace, policy, access, cluster, specific, secure, egress, traffic, ingress, obviously, connectivity, server, hubble, psyllium, across, application

### Resumo baseado na transcript

thank you all for attending this late afternoon session before the end of the day in the booth crawl my name is Raymond Dion I'm very happy to present here about adopting Network policies in highly secure environments the agenda today is this is not a network policy 101 this is more like a talk how we see our customers dealing with adopting Network policies in the in the fields and how you can use for example cilium evpf and Hubble our Hubble UI and harbor CLI to basically observe it's really quick this is live flows shows live actually the fqdns it's trying to reach out so now using Hubble UI and using this simple DNS policy I learned that it's reaching out to celine.io and isovan.com and in this case that's fine and so let's allow that and we also learned in my previous step that it needs to access psyllium.io and isovariant.com on Port 443 also note that I'm adding This [Music] Server matching labels and obviously on Port 80 save this apply it and then we

### Excerpt da transcript

thank you all for attending this late afternoon session before the end of the day in the booth crawl my name is Raymond Dion I'm very happy to present here about adopting Network policies in highly secure environments the agenda today is this is not a network policy 101 this is more like a talk how we see our customers dealing with adopting Network policies in the in the fields and how you can use for example cilium evpf and Hubble our Hubble UI and harbor CLI to basically observe traffic and adopt Network policies in your classes effectively without blocking your applications so I'll start with some strategies tips and tricks and approaches to adult network policies and then talk about psyllium features that matter for using that and looking at observability as a superpower to make sure that you're able to enforce security and observe flows to ensure your compliance I've prepared a little demo so I hope the demo gods are with me so I can show a little example how you can use your Hubble for example to secure your workloads my name is Raymond young I'm field CTO for emea at isofeland that means that we also work with a lot of customers both open source and our Enterprise release who are adopting psyllium and eppf in their environments to secure those environments as well can I see hence how many of you know about psyllium all quite about quite a lot okay so how many of you know ebpf and how many of you are already applying Network policies in their environments okay a little less hence okay great so that's the whole purpose of today uh to give you that tips um so isofilence is the company behind sidium and ebpf we created psyllium we open source psyllium and we're still contributing to the celium open source release and we also maintain ebpf I will talk about Cinema ebpf a bit later so let's start with having a bit of a talk about strategies for Designing Network policies what we see is that a lot of companies struggle with adopting Network policies you want to avoid allowing everything a lot of companies want to have a zero trust based approach but in the meantime you also do not want to block your application teams and you may want to make the onboarding of your application as easy as possible but you also want to prevent application teams themselves to allow all traffic for their namespaces are going in and going out so you need to have some constraints there put in in your system to avoid structure feeding and you also want to a lot of our companies al
