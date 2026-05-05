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
themes: ["AI ML", "Security"]
speakers: ["Andrew Martin", "ControlPlane"]
sched_url: https://kccncna2022.sched.com/event/182KI/untrusted-execution-attacking-the-cloud-native-supply-chain-andrew-martin-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=Untrusted+Execution%3A+Attacking+the+Cloud+Native+Supply+Chain+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Untrusted Execution: Attacking the Cloud Native Supply Chain - Andrew Martin, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Detroit
- Speakers: Andrew Martin, ControlPlane
- Schedule: https://kccncna2022.sched.com/event/182KI/untrusted-execution-attacking-the-cloud-native-supply-chain-andrew-martin-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=Untrusted+Execution%3A+Attacking+the+Cloud+Native+Supply+Chain+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Untrusted Execution: Attacking the Cloud Native Supply Chain.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182KI/untrusted-execution-attacking-the-cloud-native-supply-chain-andrew-martin-controlplane
- YouTube search: https://www.youtube.com/results?search_query=Untrusted+Execution%3A+Attacking+the+Cloud+Native+Supply+Chain+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vu_qMthpww8
- YouTube title: Untrusted Execution: Attacking the Cloud Native Supply Chain - Andrew Martin, ControlPlane
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/untrusted-execution-attacking-the-cloud-native-supply-chain/vu_qMthpww8.txt
- Transcript chars: 31328
- Keywords: supply, security, attack, actually, control, threat, controls, source, infrastructure, threats, native, software, compromise, integrity, signing, modeling, course, systems

### Resumo baseado na transcript

good afternoon everybody and welcome thank you preemptively for your attention welcome to untrusted execution at attacking the cloud native supply chain so hot right now and I hope to give you an attack driven defensive perspective I'm Andy I'm CEO at control plane uh very lucky to have a number of my excellent colleagues here today we have a booth please do stop by we've got all sorts of good stuff including the supply chain security best practices flash cards including such interesting things as ebpf for observability content

### Excerpt da transcript

good afternoon everybody and welcome thank you preemptively for your attention welcome to untrusted execution at attacking the cloud native supply chain so hot right now and I hope to give you an attack driven defensive perspective I'm Andy I'm CEO at control plane uh very lucky to have a number of my excellent colleagues here today we have a booth please do stop by we've got all sorts of good stuff including the supply chain security best practices flash cards including such interesting things as ebpf for observability content addressability for immutable artifacts everything from Vex through to Frisco and we'll talk about some of those Concepts I am also the author of hacking kubernetes along with my esteemed friend Mr Michael hasenblass we'll do a book signing at half past four so that is all the advertising briefly out of the way I'm lucky to be involved with the cncf's technical Advisory Group on security where we assure the open source cncf projects that look to achieve sandbox incubation the goal there is to provide a safe space to collaborate with maintainers and some of the things that we'll talk about today involving threat modeling and best practice are how we interface with those projects coming through I'm also in my spare time CSO at open UK open UK is an open source advocacy group we are a charity that asks UK governments and the private sector to remunerate open source maintainers for their time for shipping security fixes and helping to advise the UK government on policy my background is Development I've I've also got a deep of course security interest but also these things have to be usable there's no point shipping a security control that is constrictive that has no quantifiable benefits and ultimately that has a long-term maintenance burden on the users of the system developer retention is important and needless security controls are diametrically opposed to that the book is also available as a PDF for download I lied when I said I was done Shilling for myself that is the end of it I assure you uh control plane we are security specialists and open source Cloud native Advocates we have just opened an office in North America we're about to open an office in Asia Pacific in New Zealand if Cloud native security challenges nice people and interesting work are your bag please do come have a word with all my colleagues to understand what we do okay will we talk about the supply chain problem what is it why is it a problem how is it directly ex
