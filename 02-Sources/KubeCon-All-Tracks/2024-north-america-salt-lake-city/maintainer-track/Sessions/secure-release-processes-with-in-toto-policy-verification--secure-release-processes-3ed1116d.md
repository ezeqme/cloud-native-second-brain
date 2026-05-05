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
speakers: ["John Kjell", "TestifySec", "Aditya Sirish A Yelgundhalli", "New York University"]
sched_url: https://kccncna2024.sched.com/event/1hoxI/secure-release-processes-with-in-toto-policy-verification-john-kjell-testifysec-aditya-sirish-a-yelgundhalli-new-york-university
youtube_search_url: https://www.youtube.com/results?search_query=Secure+Release+Processes+with+in-Toto+Policy+Verification+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Secure Release Processes with in-Toto Policy Verification - John Kjell, TestifySec & Aditya Sirish A Yelgundhalli, New York University

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: John Kjell, TestifySec, Aditya Sirish A Yelgundhalli, New York University
- Schedule: https://kccncna2024.sched.com/event/1hoxI/secure-release-processes-with-in-toto-policy-verification-john-kjell-testifysec-aditya-sirish-a-yelgundhalli-new-york-university
- Busca YouTube: https://www.youtube.com/results?search_query=Secure+Release+Processes+with+in-Toto+Policy+Verification+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Secure Release Processes with in-Toto Policy Verification.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxI/secure-release-processes-with-in-toto-policy-verification-john-kjell-testifysec-aditya-sirish-a-yelgundhalli-new-york-university
- YouTube search: https://www.youtube.com/results?search_query=Secure+Release+Processes+with+in-Toto+Policy+Verification+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-tGn0kEeA4M
- YouTube title: Secure Release Processes with in-Toto Policy Verification - John Kjell, Aditya Sirish A Yelgundhalli
- Match score: 0.82
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/secure-release-processes-with-in-toto-policy-verification/-tGn0kEeA4M.txt
- Transcript chars: 29499
- Keywords: supply, software, process, policies, pipeline, security, source, policy, verification, witness, intoto, everything, information, stations, actually, secure, processes, framework

### Resumo baseado na transcript

Welcome to our talk on secure release processes with inal policy verification uh my name is adtia I'm a PhD student at New York University I'm a maintainer of the inal framework I I'm also a maintainer of a number of other software supply chain security related projects like giu and get sign six or G sign the salsa specification so on and I've contributed to related efforts like the tff project and the cncf uh tax security uh software Supply CH security working group uh that hi I'm uh

### Excerpt da transcript

Welcome to our talk on secure release processes with inal policy verification uh my name is adtia I'm a PhD student at New York University I'm a maintainer of the inal framework I I'm also a maintainer of a number of other software supply chain security related projects like giu and get sign six or G sign the salsa specification so on and I've contributed to related efforts like the tff project and the cncf uh tax security uh software Supply CH security working group uh that hi I'm uh John and I'm a a director of Open Source at testify Su uh in addition to that I'm a cncf security tag uh Tech lead and maintainer of witness in Arista we've got these cool t-shirts um and also es bomit which is in open ssf which combines intoto attestations and S bombs uh and then we just released a new version uh through tag security of the V2 of supply chain security best practices so definitely check that out if you haven't yet um yeah so we'll go ahead and get started software supply chain attacks um so kind of looking at this starting out defining what it is we mean by a software supply chain attack you have uh or you know software supply chain before we talk about the attack part a collection of systems devices organizations and people people which produce prod a final software product so as uh most folks here probably know there's a lot of stuff that goes into a release of software and it's more than just ones and zeros uh it's about how it gets there the people who got it there uh the processes with which it went through to get there the devices the hardware the software all of those things so how do we what happens or or how do we Define an attack on this process as when one or more weaknesses in the components of the software supply chain are compromised to introduce alterations into the final software product so you know basically whatever you produce at the end is not what you expect and we've just seen a couple of software supply chain attacks in recent memory uh one of the things that uh Santiago who did the keynote this morning uh he helps maintain this catalog of uh supply chain compromises under the cncf tag security repo so if you want to go and read about uh a whole bunch of different software supply chain attacks this is a good place to check that out and it's not getting better right it's just continually getting worse and so we can see uh from this the the sonot type uh instead of supply chain security report this is the number of malicious packages disc
