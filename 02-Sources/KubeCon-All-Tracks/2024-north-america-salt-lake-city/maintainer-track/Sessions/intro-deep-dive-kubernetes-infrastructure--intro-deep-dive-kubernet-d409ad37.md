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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Arnaud Meukam", "Independent", "Mahamed Ali", "Cisco"]
sched_url: https://kccncna2024.sched.com/event/1hox2/intro-deep-dive-kubernetes-infrastructure-arnaud-meukam-independent-mahamed-ali-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Intro+%26+Deep+Dive+-+Kubernetes+Infrastructure+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Intro & Deep Dive - Kubernetes Infrastructure - Arnaud Meukam, Independent & Mahamed Ali, Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Arnaud Meukam, Independent, Mahamed Ali, Cisco
- Schedule: https://kccncna2024.sched.com/event/1hox2/intro-deep-dive-kubernetes-infrastructure-arnaud-meukam-independent-mahamed-ali-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Intro+%26+Deep+Dive+-+Kubernetes+Infrastructure+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Intro & Deep Dive - Kubernetes Infrastructure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hox2/intro-deep-dive-kubernetes-infrastructure-arnaud-meukam-independent-mahamed-ali-cisco
- YouTube search: https://www.youtube.com/results?search_query=Intro+%26+Deep+Dive+-+Kubernetes+Infrastructure+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XZlalBACTSg
- YouTube title: Intro & Deep Dive - Kubernetes Infrastructure - Arnaud Meukam, Independent & Mahamed Ali, Cisco
- Match score: 0.731
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/intro-deep-dive-kubernetes-infrastructure/XZlalBACTSg.txt
- Transcript chars: 10381
- Keywords: basically, infrastructure, currently, migration, provider, access, registry, trying, future, running, various, accounts, cluster, everybody, maintainer, assets, testing, google

### Resumo baseado na transcript

hello everybody um Welcome to our talk on the communities infrastructure let's see all right so we're going to be talking about the kuber projects Cloud infrastructure and the kind of things that we've been doing lately all right so introductions uh my name is Muhammad I work at Thousand I by Cisco I am a sias infr tech lead I am ative maintainer and I'm also a cncf Ambassador um and my name my name is is an mukam I am currently independent and I'm the SE and Tech project because we have to pay for the erress cost of it and currently that's why we use fasty right now okay thanks so the other I I would say the next step for the Sig will be the migration from GCR to ARA registry

### Excerpt da transcript

hello everybody um Welcome to our talk on the communities infrastructure let's see all right so we're going to be talking about the kuber projects Cloud infrastructure and the kind of things that we've been doing lately all right so introductions uh my name is Muhammad I work at Thousand I by Cisco I am a sias infr tech lead I am ative maintainer and I'm also a cncf Ambassador um and my name my name is is an mukam I am currently independent and I'm the SE and Tech lead for the community infrastructure also one of the Rel manager for the project all right so for those of you who don't know s kubernets infrastructure manages the kuber projects Cloud infrastructure so we have a couple of critical services that we run so we're on the Project's image registry called registry. iio should be very familiar to everybody here we also have the prow CI that I'm going to share a screenshot off in a second but that's the primary CI that we use at kubet it's a custom built CI that we've built um we also have DL does.io that serves our blobs or binary assets of all the kuet binaries um and we also have some miscellaneous Cloud infrastructure that we're running on AWS Azure gcp and digital oan um these are primarily clusters that we use for end testing and we have some assets that required to test Cloud hardware for various CL provider features um all right so to you as you can see here this is the community CI dashboard so on most PRS um in our kuber and C 6 GG you will see a link for a job that will take you to here so this is a list of all our jobs how long they be running and what's going on um this project has its own dedicated repository um plus the configuration for it lives in this GI up repa all right as as I said earlier we run a lot of cloud infrastructure so we are adopting some Modern tooling so we're using AO City to manage our clusters so we've got like four or five of those um running various bit of applications all right so six seven months ago I stood up here in Paris um at the previous keepon mentioning all the cool things we were doing this year so we said we were going to work on the CI migration so for context the CU project is 10 years old um and Google was the first company that founded it and they were nice enough to run the CI for it in their private Cloud accounts right so we've moved all of that out to community owned accounts so that was the migration that we're planning on doing this year we managed to do that sometime in August um we also had
