---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["Tim Ramlot", "Ashley Davis", "Venafi"]
sched_url: https://kccncna2024.sched.com/event/1i7rz/spiffe-the-easy-way-universal-x509-and-jwt-identities-using-cert-manager-tim-ramlot-ashley-davis-venafi
youtube_search_url: https://www.youtube.com/results?search_query=SPIFFE+the+Easy+Way%3A+Universal+X509+and+JWT+Identities+Using+cert-manager+CNCF+KubeCon+2024
slides: []
status: parsed
---

# SPIFFE the Easy Way: Universal X509 and JWT Identities Using cert-manager - Tim Ramlot & Ashley Davis, Venafi

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Salt Lake City
- Speakers: Tim Ramlot, Ashley Davis, Venafi
- Schedule: https://kccncna2024.sched.com/event/1i7rz/spiffe-the-easy-way-universal-x509-and-jwt-identities-using-cert-manager-tim-ramlot-ashley-davis-venafi
- Busca YouTube: https://www.youtube.com/results?search_query=SPIFFE+the+Easy+Way%3A+Universal+X509+and+JWT+Identities+Using+cert-manager+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre SPIFFE the Easy Way: Universal X509 and JWT Identities Using cert-manager.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rz/spiffe-the-easy-way-universal-x509-and-jwt-identities-using-cert-manager-tim-ramlot-ashley-davis-venafi
- YouTube search: https://www.youtube.com/results?search_query=SPIFFE+the+Easy+Way%3A+Universal+X509+and+JWT+Identities+Using+cert-manager+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=De2o-urGpQk
- YouTube title: SPIFFE the Easy Way: Universal X509 and JWT Identities Using cert-manager - Tim Ramlot, Ashley Davis
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/spiffe-the-easy-way-universal-x509-and-jwt-identities-using-cert-manag/De2o-urGpQk.txt
- Transcript chars: 33951
- Keywords: spiffy, manager, actually, workload, exchange, certificate, driver, container, running, support, pretty, identity, authenticate, request, already, socket, basically, directly

### Resumo baseado na transcript

uh great hello everyone uh welcome to spiffy the easy way um I appreciate that it is the last talk of cubec con which uh makes it extra special that you've all turned up I I wasn't sure how many to expect and I'm seeing a lot of faces smiling back at me that's always lovely I actually see a lot of faces that I recognize from the conference as well people that have dropped by the C manager Booth uh it was great to see so many of you

### Excerpt da transcript

uh great hello everyone uh welcome to spiffy the easy way um I appreciate that it is the last talk of cubec con which uh makes it extra special that you've all turned up I I wasn't sure how many to expect and I'm seeing a lot of faces smiling back at me that's always lovely I actually see a lot of faces that I recognize from the conference as well people that have dropped by the C manager Booth uh it was great to see so many of you uh Dro by uh my name's Ash this is Tim uh we're both software engineers at Veni which is now a cyber company uh as as you may have guessed from the title of this slide we're here to talk about spiffy Ander manager so let's jump into that make sure that we're both on the we're all on the same page so this is the slide that we throw on pretty much any talk we do about C manager um an important change to this slide though is that it says cntf graduated now which is what we announced here in Salt Lake City this year um this is the the first cubec con since we hit graduation and it's a huge mil stone for the project um Zone Manager is we like to say the easiest way to manage x509 certificates in kubernetes um being a graduated project is kind of a stamp of approval from the cntf that we're we're we're issuing issuing those certificates correctly and that's good um we've got some big numbers which is also a customary for this slide but we an important one for me is that we hear maybe 80 to 90% of clusters actually install SE manager by default which is crazy to think about um graduated is actually the same level that kubernetes itself is at so so again awesome to to be at that level um it was a long road we're really happy to be here um so yeah we'll obviously be using SE manager in this talk and talking about that more but um we're also going to be talking about a different cncf graduated project which is spiffy um so spiffy if you're not familiar is a uh sort of a specification for uh identity um specifically it it defines a iy ID which is sort of like an identity for a a workload or a machine um which is a sort of known format that you can pass and then use if you want to um it also defines a wrapper for that identity which is called an esid so uh your spiffy identity is wrapped inside an sfid and that sfid can be of two different types it's there's x509 which is the same format that CT manager uses to issue CTS for your website say and JWT or jot uh which is the same format that causes numerous security issues around the world whe
