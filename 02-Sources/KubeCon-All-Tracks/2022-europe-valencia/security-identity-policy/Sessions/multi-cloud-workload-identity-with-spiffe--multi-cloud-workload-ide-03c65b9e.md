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
themes: ["Security"]
speakers: ["Jake Sanders", "Charlie Egan", "Jetstack"]
sched_url: https://kccnceu2022.sched.com/event/yttX/multi-cloud-workload-identity-with-spiffe-jake-sanders-charlie-egan-jetstack
youtube_search_url: https://www.youtube.com/results?search_query=Multi-Cloud+Workload+Identity+With+SPIFFE+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Multi-Cloud Workload Identity With SPIFFE - Jake Sanders & Charlie Egan, Jetstack

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: Spain / Valencia
- Speakers: Jake Sanders, Charlie Egan, Jetstack
- Schedule: https://kccnceu2022.sched.com/event/yttX/multi-cloud-workload-identity-with-spiffe-jake-sanders-charlie-egan-jetstack
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-Cloud+Workload+Identity+With+SPIFFE+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Multi-Cloud Workload Identity With SPIFFE.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yttX/multi-cloud-workload-identity-with-spiffe-jake-sanders-charlie-egan-jetstack
- YouTube search: https://www.youtube.com/results?search_query=Multi-Cloud+Workload+Identity+With+SPIFFE+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vKRUq56xDiE
- YouTube title: Multi-Cloud Workload Identity With SPIFFE - Jake Sanders & Charlie Egan, Jetstack
- Match score: 0.781
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/multi-cloud-workload-identity-with-spiffe/vKRUq56xDiE.txt
- Transcript chars: 34483
- Keywords: identity, spiffy, workload, server, credentials, connector, manager, running, identities, workloads, provider, available, anything, actually, application, thanks, document, another

### Resumo baseado na transcript

so hi everyone it's great to be here personally kubecon and thanks for sticking around with us like i know it's late on a friday and everyone just wants to go but we're here to talk to you about multi-cloud workload identity with spiffy i'm jake i am one of the site manager maintainers um interested in all things identity and x509 and hey i'm charlie i work on the enterprise side of jetstack product and i'm also interested in all things authentication and authorization we're both senior software engineers

### Excerpt da transcript

so hi everyone it's great to be here personally kubecon and thanks for sticking around with us like i know it's late on a friday and everyone just wants to go but we're here to talk to you about multi-cloud workload identity with spiffy i'm jake i am one of the site manager maintainers um interested in all things identity and x509 and hey i'm charlie i work on the enterprise side of jetstack product and i'm also interested in all things authentication and authorization we're both senior software engineers uh working at jetstack and jetstart product and are both interested in spiffy we think spiffy's really great and we're interested in trying to encourage more adoption in the in the technology and that's why we're doing this talk during a company hackathon at the end of last year we worked on a project that allowed was based on using spiffy ids to improve the developer experience for cross-cloud identities or use of cross-cloud apis for cross-cloud workloads and the work that we're presenting today is based on that so we're going to have a presentation where we're going to explain about how we think about workload identity and what that means for us and then we're going to have um a short and explain what we've built and have a short demo of that and you'll also be able to get we'll also share a link to our code at the end if you're interested in having a look yourselves it's a proof of concept but the code will be there so what do we think about workflow identity what what is a workload identity so [Music] an identity is a way for a workload to prove who it is prove its authenticity to other workloads and other anything that it may be communicating with so we believe that a workload identity workload should be issued this identity just by existing just by running in a cluster just by running anywhere it's not something that it should you shouldn't have to have anything that it knows uh anything that it's any secret that should be given beforehand it's something that it should get just by existing by running in some environment so contrasting this to what we often see people doing uh with even with kubernetes workloads is they're putting secrets in there in their deployments they're including secret tokens to talk to other services like we we believe that those aren't identities and identity is a different thing an identity is something that you have just by existing so um yeah the problem of course you many of you will be aware of you know if you're tryin
