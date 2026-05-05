---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Open Interfaces + Interoperability"
themes: ["AI ML"]
speakers: ["Josh Dolitsky", "Chainguard", "Sajay Antony", "Microsoft"]
sched_url: https://kccncna2022.sched.com/event/182G5/its-complicated-relationships-between-objects-in-oci-registries-josh-dolitsky-chainguard-sajay-antony-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=It%E2%80%99s+Complicated%3A+Relationships+Between+Objects+In+OCI+Registries+CNCF+KubeCon+2022
slides: []
status: parsed
---

# It’s Complicated: Relationships Between Objects In OCI Registries - Josh Dolitsky, Chainguard & Sajay Antony, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Open Interfaces + Interoperability]]
- Temas: [[AI ML]]
- País/cidade: United States / Detroit
- Speakers: Josh Dolitsky, Chainguard, Sajay Antony, Microsoft
- Schedule: https://kccncna2022.sched.com/event/182G5/its-complicated-relationships-between-objects-in-oci-registries-josh-dolitsky-chainguard-sajay-antony-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=It%E2%80%99s+Complicated%3A+Relationships+Between+Objects+In+OCI+Registries+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre It’s Complicated: Relationships Between Objects In OCI Registries.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182G5/its-complicated-relationships-between-objects-in-oci-registries-josh-dolitsky-chainguard-sajay-antony-microsoft
- YouTube search: https://www.youtube.com/results?search_query=It%E2%80%99s+Complicated%3A+Relationships+Between+Objects+In+OCI+Registries+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VZckJNkJ0nQ
- YouTube title: It’s Complicated: Relationships Between Objects In OCI Registries - Josh Dolitsky & Sajay Antony
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/its-complicated-relationships-between-objects-in-oci-registries/VZckJNkJ0nQ.txt
- Transcript chars: 23972
- Keywords: manifest, artifact, registry, digest, attach, actually, similar, working, specific, specification, subject, called, reference, support, registries, docker, changes, cosine

### Resumo baseado na transcript

uh my name is Josh dolitsky I work at a company called chain guard come visit us in the booth area we have socks and other things um Sanjay could not make it here today um but we have a fantastic video of him doing a fantastic demo and I encourage you to watch it while it's happening and it's going to be a great presentation so uh we're going to talk today about oci which is something that I have found myself entangled in in the last several years

### Excerpt da transcript

uh my name is Josh dolitsky I work at a company called chain guard come visit us in the booth area we have socks and other things um Sanjay could not make it here today um but we have a fantastic video of him doing a fantastic demo and I encourage you to watch it while it's happening and it's going to be a great presentation so uh we're going to talk today about oci which is something that I have found myself entangled in in the last several years and we're going to talk about this um how do you connect different things inside of a registry so if you're if you're in this space or if you're in this talk right now in this room you probably know that people have been putting things into Registries in questionable ways and um that's an issue because uh tooling doesn't know how to work with that and so um so it's really a two-part it's really a two-part issue one is what I just said how do you get a list of these things that point to an image um I'll say the word s-bomb uh s-bombs s-bombs um how do you find out uh basically given an image what are the s-bombs that point to it signatures or anything else really you can you should be able to attach any type of metadata without modifying the digest of an image because that's what makes uh you know container Registries secure and let you know that nothing has been tampered with um so always use digests so exactly how are we going to get this list in the second part of that question is like an implied uh it's it's kind of implied of like you know there people are putting these things in here but how do you actually do that how are you supposed to do that in a way that um has sort of been blessed by the open container initiative and is like the recommended approach because there's been a few different ways and some are trying to be uh change the system and some of them are trying to work with the existing system and certain Registries don't have all the features uh and you'll you know you'll find flags on tools like cosine that you know help you work around these issues and it's not really it's not it's not a sustainable uh thing um so that's the problem but it's a problem that has two parts one is how do we actually do that and then I can't see uh and then but how do we actually do that with the community and so um you know for the people here who have worked in open source you can you know that there's a people that the harder part is working with people um anyone can write an amazing API and an amazing tool but ho
