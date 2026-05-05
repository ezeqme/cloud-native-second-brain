---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Aditya Sirish A Yelgundhalli", "New York University"]
sched_url: https://kccnceu2023.sched.com/event/1HySK/in-toto-attestations-and-more-for-software-supply-chain-security-aditya-sirish-a-yelgundhalli-new-york-university
youtube_search_url: https://www.youtube.com/results?search_query=In-Toto%3A+Attestations+and+More+for+Software+Supply+Chain+Security+CNCF+KubeCon+2023
slides: []
status: parsed
---

# In-Toto: Attestations and More for Software Supply Chain Security - Aditya Sirish A Yelgundhalli, New York University

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Aditya Sirish A Yelgundhalli, New York University
- Schedule: https://kccnceu2023.sched.com/event/1HySK/in-toto-attestations-and-more-for-software-supply-chain-security-aditya-sirish-a-yelgundhalli-new-york-university
- Busca YouTube: https://www.youtube.com/results?search_query=In-Toto%3A+Attestations+and+More+for+Software+Supply+Chain+Security+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre In-Toto: Attestations and More for Software Supply Chain Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HySK/in-toto-attestations-and-more-for-software-supply-chain-security-aditya-sirish-a-yelgundhalli-new-york-university
- YouTube search: https://www.youtube.com/results?search_query=In-Toto%3A+Attestations+and+More+for+Software+Supply+Chain+Security+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ezV_oWBPqKw
- YouTube title: In-Toto: Attestations and More for Software Supply Chain Security - Aditya Sirish A Yelgundhalli
- Match score: 0.895
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/in-toto-attestations-and-more-for-software-supply-chain-security/ezV_oWBPqKw.txt
- Transcript chars: 30715
- Keywords: software, supply, internal, witness, policy, attestation, actually, metadata, pipeline, framework, layout, number, verify, attestations, security, artifacts, working, projects

### Resumo baseado na transcript

hey everyone um my name is Aditya I'm a PhD student at New York University and I'm going to be talking about in Toto at the stations and more for software supply chain security and you know whenever we do talk about in Toto we always do a quick primer on what software supply chain attacks are uh so a software supply chain as I'm guessing most of you in this room are intimately familiar with in given given everything that's happened over the last couple of years is everything

### Excerpt da transcript

hey everyone um my name is Aditya I'm a PhD student at New York University and I'm going to be talking about in Toto at the stations and more for software supply chain security and you know whenever we do talk about in Toto we always do a quick primer on what software supply chain attacks are uh so a software supply chain as I'm guessing most of you in this room are intimately familiar with in given given everything that's happened over the last couple of years is everything the people the artifacts all of the different systems that come together to produce a piece of software and an attack is a compromise of any of the many different things that came together in creating a software artifact whether it was at you know the person a human and loop who is part of creating the software or compromise of a build system or something like that and and the attacks and and this compromise has to be you know very targeted at compromising the consumer of whatever was being built right so this the the there's been a 742 increase we've seen this number from sonotypes Lost report on the state of the software supply chain the numbers probably going to go up at which point we'll update these slides by probably around kubecon North America just went uh which is around when the report comes out and we've seen a lot of these attacks over the years and with the internal team were used to track them uh in what's called a you know a catalog of software supply chain security compromises which we donated to the cncf tax security software supply chain security working group uh it's really helpful and I highly recommend you all check it out it's being updated by the tax security working group uh over the years and uh we used a lot of these incidents to try uh to you know to drive the development of the internal framework so yeah definitely recommend checking this resource out uh and as a response to all of these software supply chain security incidents uh we've seen many solutions emerge which we can I think broadly categorize into three different buckets right we've got projects that are focused on uh the on generating various types of evidence of what happened during your software supply chain execution whether that's like prominence of a build step that you'd get with something like salsa generated from your CI system uh are you know uh the npm logo I threw up today because of npm's announcement from yesterday that they're uh now you can now generate prominence from during npm bu
