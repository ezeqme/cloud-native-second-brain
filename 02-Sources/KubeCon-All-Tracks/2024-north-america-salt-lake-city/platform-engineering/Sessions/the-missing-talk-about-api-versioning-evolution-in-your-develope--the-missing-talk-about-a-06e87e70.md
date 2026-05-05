---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Stefan Schimanski", "Upbound", "Sergiusz Urbaniak", "Independent"]
sched_url: https://kccncna2024.sched.com/event/1i7qn/the-missing-talk-about-api-versioning-evolution-in-your-developer-platform-stefan-schimanski-upbound-sergiusz-urbaniak-independent
youtube_search_url: https://www.youtube.com/results?search_query=The+Missing+Talk+About+API+Versioning+%26+Evolution+in+Your+Developer+Platform+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The Missing Talk About API Versioning & Evolution in Your Developer Platform - Stefan Schimanski, Upbound & Sergiusz Urbaniak, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Salt Lake City
- Speakers: Stefan Schimanski, Upbound, Sergiusz Urbaniak, Independent
- Schedule: https://kccncna2024.sched.com/event/1i7qn/the-missing-talk-about-api-versioning-evolution-in-your-developer-platform-stefan-schimanski-upbound-sergiusz-urbaniak-independent
- Busca YouTube: https://www.youtube.com/results?search_query=The+Missing+Talk+About+API+Versioning+%26+Evolution+in+Your+Developer+Platform+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The Missing Talk About API Versioning & Evolution in Your Developer Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qn/the-missing-talk-about-api-versioning-evolution-in-your-developer-platform-stefan-schimanski-upbound-sergiusz-urbaniak-independent
- YouTube search: https://www.youtube.com/results?search_query=The+Missing+Talk+About+API+Versioning+%26+Evolution+in+Your+Developer+Platform+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pHRQpqCEvU8
- YouTube title: The Missing Talk About API Versioning & Evolution in Your Developer Pl... S. Schimanski, S. Urbaniak
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-missing-talk-about-api-versioning-evolution-in-your-developer-plat/pHRQpqCEvU8.txt
- Transcript chars: 33394
- Keywords: version, versions, schema, patterns, object, pattern, everything, objects, little, basically, change, request, inside, important, versioning, server, conversion, storage

### Resumo baseado na transcript

cool so welcome to The Talk The Missing talk about API versioning and the evolution in your developer platform uh my name is sech I'm in the kubernetes ecosystem since 2016 I wrote probably way too many operators and broke way too many users with crd API versioning and that was the main motivation for this talk yeah my name is Stefan stansky I'm involved in crd work for years so lots of the things the pain you are seeing might be uh my fault um we will see but

### Excerpt da transcript

cool so welcome to The Talk The Missing talk about API versioning and the evolution in your developer platform uh my name is sech I'm in the kubernetes ecosystem since 2016 I wrote probably way too many operators and broke way too many users with crd API versioning and that was the main motivation for this talk yeah my name is Stefan stansky I'm involved in crd work for years so lots of the things the pain you are seeing might be uh my fault um we will see but we have this talk to repair everything and fix everything so there was a talk two No 3 hours ago um I an echo here is this is it okay I think so can you hear me well okay strange so there was a talk in the same track um before lunch and the title is super similar as you notice so Nick gave a very um yeah basically an introduction to the same topic but very AOG so um if you haven't seen that please watch the recording it's a great um complimentary addition to our talk all right so that's probably something that everybody of you see every day right I mean at the end of the day we are crd developers and we provision like well we develop crd apis and like we have this little silly example here with a crd of kind table uh and we have some spec with a color thickness he and some status condition with a cost and obviously on the right hand side you see the open API schema uh maybe that's something you pay a little bit less attention to every day that corresponds to it right and that's sort of like something that we do every day but something that we pay very little attention to very often is like this version um you know qualifier up there that is saying version one so let's say we want to change something in this crd we want to change the structure we want to change the schema like in this case we want to put thickness and they hate like we want to like restructure it a little bit put it under a size and maybe we want to rename like the status condition cost dollar or cost into cost dollars so we changed the schema we changed the version and we call it a day right like hands up whoever did this mistake already okay I'm I'm happy I'm not alone I did this mistake as well you just broke the user if you just go it like so okay so like what we want to show you in this talk that like it's not as easy as just slapping like a new version uh up there you have to follow certain rules and certain patterns because kubernetes has quite some amount of invariance imposed upon you um so you cannot do that unfortunately ju
