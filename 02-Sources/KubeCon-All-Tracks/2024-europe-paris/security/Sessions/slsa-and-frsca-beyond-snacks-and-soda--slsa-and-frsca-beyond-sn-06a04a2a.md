---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["Security"]
speakers: ["Christopher Hanson", "RX-M", "llc."]
sched_url: https://kccnceu2024.sched.com/event/1YeNh/slsa-and-frsca-beyond-snacks-and-soda-christopher-hanson-rx-m-llc
youtube_search_url: https://www.youtube.com/results?search_query=SLSA+and+FRSCA%3A+Beyond+Snacks+and+Soda%21+CNCF+KubeCon+2024
slides: []
status: parsed
---

# SLSA and FRSCA: Beyond Snacks and Soda! - Christopher Hanson, RX-M, llc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: France / Paris
- Speakers: Christopher Hanson, RX-M, llc.
- Schedule: https://kccnceu2024.sched.com/event/1YeNh/slsa-and-frsca-beyond-snacks-and-soda-christopher-hanson-rx-m-llc
- Busca YouTube: https://www.youtube.com/results?search_query=SLSA+and+FRSCA%3A+Beyond+Snacks+and+Soda%21+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre SLSA and FRSCA: Beyond Snacks and Soda!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNh/slsa-and-frsca-beyond-snacks-and-soda-christopher-hanson-rx-m-llc
- YouTube search: https://www.youtube.com/results?search_query=SLSA+and+FRSCA%3A+Beyond+Snacks+and+Soda%21+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Yknixoneqo4
- YouTube title: SLSA and FRSCA: Beyond Snacks and Soda! - Christopher Hanson, RX-M, llc.
- Match score: 0.805
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/slsa-and-frsca-beyond-snacks-and-soda/Yknixoneqo4.txt
- Transcript chars: 30917
- Keywords: providence, artifacts, cluster, attestation, process, registry, verify, artifact, pipeline, secret, software, tecton, chains, material, levels, tracks, source, docker

### Resumo baseado na transcript

welcome folks uh to this talk on salsa and fresa uh I subtitled it the road to unfalsifiable Providence because uh that's what I kind of believe it is and um this talk was really born out of conversations that I had with Folks at at previous conferences where there wasn't a lot of um awareness of of salsa and Fresca so I wanted to make sure that um I submitted to talk that that uh brought more awareness to both of these topics so uh that's really kind of

### Excerpt da transcript

welcome folks uh to this talk on salsa and fresa uh I subtitled it the road to unfalsifiable Providence because uh that's what I kind of believe it is and um this talk was really born out of conversations that I had with Folks at at previous conferences where there wasn't a lot of um awareness of of salsa and Fresca so I wanted to make sure that um I submitted to talk that that uh brought more awareness to both of these topics so uh that's really kind of what this is about um my name is Christopher I go by Chris I shorten everybody else's name so you're welcome to shorten mine uh I'm an a Consultants I'm an instructor and uh help folks build platforms and adopt new technologies um and it's it's been a number of years that I've been doing that so I uh helped with some of the um certifications in in the space so um like for example I helped uh write the some of the questions and and help author the cek test so if you're if you're going for that certification and it's really really hard and you want to curse my name you're welcome to do that so uh all right so what is salsa uh it it stands for supply chain level for software artifacts um it is a framework for assessing uh and communicating the the trustworthiness of software artifacts that are produced by the software supply chain so think of it as like a checklist right uh you check off a number of uh items from salsa and you can communicate that your artifacts are compliant with uh salsa levels in the supply chain uh we're going to go over those as we go through this talk uh the framework is aimed at software producers so uh there's another framework that's about ingestion consumption on the consumer side so uh this is all about you're producing artifacts for consumers Downstream they want to be able to verify that those artifacts are indeed uh what you told them you were building right and the idea is to provide that transparency to Consumers Downstream so that they can do that um and we when we build artifacts we include verifiable trust metadata with those artifacts so that they can do exactly that the there's details about how the artifacts were built uh the platform where it was built and then we cryptographically signed those um that metad data so that uh we can uh ensure that there's a guarantee about uh how that artifact was built and then the consumer can trust it so uh the salsa 1.0 standard is split into track tracks and levels uh the previous uh before 1.0 we didn't have tracks or levels but whe
