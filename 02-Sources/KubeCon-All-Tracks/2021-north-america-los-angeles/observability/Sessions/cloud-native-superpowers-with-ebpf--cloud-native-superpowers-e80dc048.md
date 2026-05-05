---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Observability"
themes: ["Observability"]
speakers: ["Liz Rice", "Isovalent"]
sched_url: https://kccncna2021.sched.com/event/lV2X/cloud-native-superpowers-with-ebpf-liz-rice-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Superpowers+with+eBPF+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Cloud Native Superpowers with eBPF - Liz Rice, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Los Angeles
- Speakers: Liz Rice, Isovalent
- Schedule: https://kccncna2021.sched.com/event/lV2X/cloud-native-superpowers-with-ebpf-liz-rice-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Superpowers+with+eBPF+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Cloud Native Superpowers with eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV2X/cloud-native-superpowers-with-ebpf-liz-rice-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Superpowers+with+eBPF+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZXDhKUeUUSs
- YouTube title: Cloud Native Superpowers with eBPF by Liz Rice
- Match score: 0.93
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/cloud-native-superpowers-with-ebpf/ZXDhKUeUUSs.txt
- Transcript chars: 23701
- Keywords: ebpf, kernel, applications, running, networking, container, network, native, programs, events, security, sidecar, powerful, packet, information, whether, mesh, actually

### Resumo baseado na transcript

excitement I introduce you to a remarkable technologist and influential leader in the cloud native ecosystem this rise as a chief open source officer at isowulin Liz has been instrumental in shaping the future of container security Cloud native applications and eppf which you will learn more about it in a minute list is a former chair of the cloud native Computing foundations technical oversight committee open UK board member AWS container hero Google developer expert and so much more to introduce her reasonable it would be a talk by

### Excerpt da transcript

excitement I introduce you to a remarkable technologist and influential leader in the cloud native ecosystem this rise as a chief open source officer at isowulin Liz has been instrumental in shaping the future of container security Cloud native applications and eppf which you will learn more about it in a minute list is a former chair of the cloud native Computing foundations technical oversight committee open UK board member AWS container hero Google developer expert and so much more to introduce her reasonable it would be a talk by itself in short she is a dedicated advocate for open source Technologies her commitment to share her expertise earned a reputation as a trusted voice in the kubernetes and container security communities this talent for breaking down technology into understandable bite sizes made her more than well recognized in the open source world and Beyond she is also the author of kubernetes security a go-to resource for understanding and implementing best practice and container security and will publish soon next month her new book learning eppf and here she is the influential and ever inspiring list rice thank you so much for that very kind introduction Max um wonderful to be here thank you everyone for joining us today in this event in support of the people in Ukraine shout out to anybody who's watching us from there so um Max has given me an amazing introduction so I don't think I really need to say any more about myself um let's make sure I'm on the right screen there we go um max also mentioned my new book it's actually already available electronically and the physical copies are in at the printers right now so I haven't seen a physical copy myself yet but it's on its way and it's called learning ebpf I've been really fascinated by this technology for quite a few years now um and today I want to share some of that I guess enthusiasm as well as knowledge I've got a ton to get through in this talk in a relatively short time so uh please do if you have questions ask them in the chat if I don't have time during the talk I will try to answer them all afterwards so the two maintainers of ebpf within the Linux kernel Alexa and Daniel were kind enough to write some really nice quotes about my book on the back and I wanted to particularly highlight this quote from Daniel that evpf started a new infrastructure movement in the cloud native space and that's really all I want to talk about today how we can make use of evpf to really get a whole
