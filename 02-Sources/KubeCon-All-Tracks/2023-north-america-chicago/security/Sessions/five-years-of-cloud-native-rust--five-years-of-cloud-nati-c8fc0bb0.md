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
speakers: ["Alex Leong", "Buoyant"]
sched_url: https://kccncna2023.sched.com/event/1R2qn/five-years-of-cloud-native-rust-alex-leong-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Five+Years+of+Cloud+Native+Rust+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Five Years of Cloud Native Rust - Alex Leong, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Chicago
- Speakers: Alex Leong, Buoyant
- Schedule: https://kccncna2023.sched.com/event/1R2qn/five-years-of-cloud-native-rust-alex-leong-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Five+Years+of+Cloud+Native+Rust+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Five Years of Cloud Native Rust.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2qn/five-years-of-cloud-native-rust-alex-leong-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Five+Years+of+Cloud+Native+Rust+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9Ro-LN2SmhY
- YouTube title: Five Years of Cloud Native Rust - Alex Leong, Buoyant
- Match score: 0.845
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/five-years-of-cloud-native-rust/9Ro-LN2SmhY.txt
- Transcript chars: 24929
- Keywords: memory, linker, reference, pointer, program, application, called, lifetime, greeter, security, control, infrastructure, compiler, vector, string, language, network, linkerd

### Resumo baseado na transcript

thank you so much Alex hi uh so hi this is five years of cloud native R so this talk was originally uh prepared uh and was going to be given by Eliza Weissman she is one of the Linker maintainers maintainers of the Linker project who works at buyant um she's a rust Enthusiast and very very cool person but unfortunately she couldn't be here for illness so I have taken over uh my name is Alex I'm also a Linker maintainer I also work at buoyant um I'm

### Excerpt da transcript

thank you so much Alex hi uh so hi this is five years of cloud native R so this talk was originally uh prepared uh and was going to be given by Eliza Weissman she is one of the Linker maintainers maintainers of the Linker project who works at buyant um she's a rust Enthusiast and very very cool person but unfortunately she couldn't be here for illness so I have taken over uh my name is Alex I'm also a Linker maintainer I also work at buoyant um I'm also a rest Enthusiast no comment on if I'm cool uh but what I want to talk about today is kind of I want to give some background on kind of how the F last five years have gone for the linardy project with respect to us adopting rust so we decided about 5 years ago to adopt rust as the language to write the linqu proxy in uh and that was a very kind of controversial or or big decision at the time so I wanted to talk about why we did that and talk about how that went and kind of uh what the outcomes of that would be would uh have been and I want to talk about why that kind of matters to people who are not Linker maintainers and what it means kind of for the ecosystem in general uh so number one why did we decide to use rust in first place uh so first of all I've been talking about being a Linker maintainer link is the Open Source service mesh part of the cncf um do everyone know is everyone familiar with with Linker have people heard of this a few hands go up yeah so Linker is a service mesh um after having been at coupon for a few years now very good at explaining what a service mesh is very quickly to people whether they like it or not um so the idea here is that you have a proxy uh that acts as a sidecar container you put one of those in every pod in your cluster and then all of the network traffic for that pod that's going in or out goes through that proxy and so because that proxy can detect what protocol it is it can see whether it's HTTP or TCP and it can do all kinds of intelligent things with it like it can transparently add mutually authenticated TLS onto that connection without the application needing to kind of do any work to make that happen uh it can do intelligent latency aware load balancing based on the actual observed latencies that it sees for real request data um it can add observability circuit breakers all kinds of really cool stuff and so Linker is infrastructure and there's two different things I mean by this uh number one Linker is Network infrastructure for your application so anytime yo
