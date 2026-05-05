---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Byron Ruth", "Synadia"]
sched_url: https://kccncna2025.sched.com/event/27NlR/state-of-nats-scale-performance-and-flexibility-byron-ruth-synadia
youtube_search_url: https://www.youtube.com/results?search_query=State+of+NATS%3A+Scale%2C+Performance%2C+and+Flexibility+CNCF+KubeCon+2025
slides: []
status: parsed
---

# State of NATS: Scale, Performance, and Flexibility - Byron Ruth, Synadia

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Byron Ruth, Synadia
- Schedule: https://kccncna2025.sched.com/event/27NlR/state-of-nats-scale-performance-and-flexibility-byron-ruth-synadia
- Busca YouTube: https://www.youtube.com/results?search_query=State+of+NATS%3A+Scale%2C+Performance%2C+and+Flexibility+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre State of NATS: Scale, Performance, and Flexibility.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NlR/state-of-nats-scale-performance-and-flexibility-byron-ruth-synadia
- YouTube search: https://www.youtube.com/results?search_query=State+of+NATS%3A+Scale%2C+Performance%2C+and+Flexibility+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YQ5mQ9dfDVw
- YouTube title: State of NATS: Scale, Performance, and Flexibility - Byron Ruth, Synadia
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/state-of-nats-scale-performance-and-flexibility/YQ5mQ9dfDVw.txt
- Transcript chars: 33680
- Keywords: stream, little, message, actually, basically, mirror, client, publish, create, always, single, consumer, trying, messages, sequence, communication, second, cluster

### Resumo baseado na transcript

um very happy with with learning the technology and um the creator of NATS is actually sitting right over there Derek Collison and so [clears throat] can say hello after the talk. Um I'm a Nat NATS project maintainer uh under the CNCF and fun fact I I was in uh pediatric research for 14 years prior to actually getting uh joining Cadia and I used NATS actually while I was there. Um there's there's a bunch of you know roles involved when you're building systems and that's sort of originated from this idea of starting simple I need to solve this sort of like core plumbing messaging problem and then it sort of grew out from And there's a lot of advantages of that which flow into sort of the architects and operator roles because as a developer, you're like, I need to solve my problem. You could start on your laptop, and this is sort of the beauty of NATS of how it's designed, and I'll show this later um, in the in the talk. All of this stuff is baked directly into nats you know out of the box and that's you know very much intentionally by design.

### Excerpt da transcript

Okay. Hello everybody. Try to make this exciting in this big room. So I'm um deal with the deal with the echo a little bit. So I'm uh Byron Ruth. I um am the VP of uh product and engineering at Cadia. I've been a NATS user and um long before joining Cenadia. um very happy with with learning the technology and um the creator of NATS is actually sitting right over there Derek Collison and so [clears throat] can say hello after the talk. Um I'm a Nat NATS project maintainer uh under the CNCF and fun fact I I was in uh pediatric research for 14 years prior to actually getting uh joining Cadia and I used NATS actually while I was there. So, quick quick show of hands. Um, who who knows Nats? Um, first of all, just put your hand up if you know if you've heard of NATS at all. Okay, keep your hands up. Who is um dabbling with it and building little applications with it, trying it out on the side? Okay. Who's using it in production? Oh, so some people actually put their hands back up. That's interesting. Okay. And who hasn't tried it at all?

You just heard of it. Nice. All right. Perfect. That's a very nice mix. All right. So, I'm going to go through a few, you know, quick intro slides. This is a maintainer track talk, so I want to make sure that everyone's sort of like caught up generally, and then we're going to sort of do like a state of NATS, what has been going on, uh, this past year. Uh so generally as a project um as we know it's a incubating incubating CNCF project we are um trying to move forward with the graduation process um from a purely you know there's a whole ecosystem around this. So there's a net server which is sort of the core project that has been contributed. There's a bunch of client libraries. There's the 11 official ones. There's a whole bunch of community ones that have been um contributed which is which is great and available on GitHub uh that are open source. Our our community is massive on Slack. Um we have Google groups, we have Slack, we have different channels for communication which has been fantastic. Um, at any given week there's probably 400 to 500 active people on Slack to answer questions and help you out and get you started if you're completely new or if you're advanced and you're like I have no idea what's going on.

All of the Senadia maintainers are also in the Slack actively uh every day. uh so you can you know ask us questions and you know there's a lot of downloads there's a lot of open source usage around that and you kn
