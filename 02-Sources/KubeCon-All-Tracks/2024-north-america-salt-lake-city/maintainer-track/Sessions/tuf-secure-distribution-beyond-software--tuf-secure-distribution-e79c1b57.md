---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Marina Moore", "Independent"]
sched_url: https://kccncna2024.sched.com/event/1hovM/tuf-secure-distribution-beyond-software-marina-moore-independent
youtube_search_url: https://www.youtube.com/results?search_query=TUF%3A+Secure+Distribution+Beyond+Software+CNCF+KubeCon+2024
slides: []
status: parsed
---

# TUF: Secure Distribution Beyond Software - Marina Moore, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Marina Moore, Independent
- Schedule: https://kccncna2024.sched.com/event/1hovM/tuf-secure-distribution-beyond-software-marina-moore-independent
- Busca YouTube: https://www.youtube.com/results?search_query=TUF%3A+Secure+Distribution+Beyond+Software+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre TUF: Secure Distribution Beyond Software.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hovM/tuf-secure-distribution-beyond-software-marina-moore-independent
- YouTube search: https://www.youtube.com/results?search_query=TUF%3A+Secure+Distribution+Beyond+Software+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TxoowCvgt4w
- YouTube title: TUF: Secure Distribution Beyond Software - Marina Moore, Independent
- Match score: 0.837
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tuf-secure-distribution-beyond-software/TxoowCvgt4w.txt
- Transcript chars: 22559
- Keywords: software, metadata, actually, secure, supply, little, version, distribution, distribute, signed, course, snapshot, security, attestations, signatures, signature, distributing, exciting

### Resumo baseado na transcript

so I'm here today to talk about tough or the update framework um and specifically how it can be used to secure distribution of more than just software um I'm Marina um work at a company called Thea and yeah excited to talk to you all today um here's a little bit more about me um I do a lot of work as an open source maintainer as well as a member of the the cncf community as part of the uh technical Advisory Group for security um recently graduated

### Excerpt da transcript

so I'm here today to talk about tough or the update framework um and specifically how it can be used to secure distribution of more than just software um I'm Marina um work at a company called Thea and yeah excited to talk to you all today um here's a little bit more about me um I do a lot of work as an open source maintainer as well as a member of the the cncf community as part of the uh technical Advisory Group for security um recently graduated with a PhD in um which with which focused on kind of software supply chain security and a little bit of the stuff we're going to talk about today and currently doing security research at adir with some of these fantastic folks um so here's what we're going to talk about today I'm sure a lot of you have heard about this whole software supply chain thing it's it's very popular right now and all this different type of metadata that you're supposed to have with your um order to use to secure your software supply chain so instead of just having to distribute this one image to everybody who wants to use it you now have all of this other information that's also super important and needs to be distributed to people as well this includes things like es bombs that talks about the dependencies of the software things like um attestations um that talk about you know who who did the build process you know were those were those machines hardened was it was the software signed um Vex documents which kind of go along with the es bombs to talk about the different you know the different vulnerabilities that a piece of software might have and these ones are especially um frustrating because they do change over time right as new more vulnerabilities are discovered in Old software you need to make sure your Vex documents is staying up to date and your policy that you use to verify to make sure that all those other things are actually um what you want them to be before you deploy a piece of software so how do we make sure that we get all of this information all this great useful security metadata actually to the consumer of the software that's kind of the piece of it we're going to talk about today um why why do we have to talk about security of medat distribution you just send it over the network right you just you take it and you send it so I'm talking about esoms just as as an example but this could be any of those pieces of metadata so this is what you want you want the software producer to make an s bomb and for now we're gonna as
