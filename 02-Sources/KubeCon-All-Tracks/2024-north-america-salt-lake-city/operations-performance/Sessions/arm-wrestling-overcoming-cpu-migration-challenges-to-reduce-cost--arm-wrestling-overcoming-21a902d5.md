---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["AI ML", "Storage Data", "SRE Reliability"]
speakers: ["Laurent Bernaille", "Eric Mountain", "Datadog"]
sched_url: https://kccncna2024.sched.com/event/1i7kU/arm-wrestling-overcoming-cpu-migration-challenges-to-reduce-costs-laurent-bernaille-eric-mountain-datadog
youtube_search_url: https://www.youtube.com/results?search_query=ARM-Wrestling%3A+Overcoming+CPU+Migration+Challenges+to+Reduce+Costs+CNCF+KubeCon+2024
slides: []
status: parsed
---

# ARM-Wrestling: Overcoming CPU Migration Challenges to Reduce Costs - Laurent Bernaille & Eric Mountain, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Laurent Bernaille, Eric Mountain, Datadog
- Schedule: https://kccncna2024.sched.com/event/1i7kU/arm-wrestling-overcoming-cpu-migration-challenges-to-reduce-costs-laurent-bernaille-eric-mountain-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=ARM-Wrestling%3A+Overcoming+CPU+Migration+Challenges+to+Reduce+Costs+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre ARM-Wrestling: Overcoming CPU Migration Challenges to Reduce Costs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kU/arm-wrestling-overcoming-cpu-migration-challenges-to-reduce-costs-laurent-bernaille-eric-mountain-datadog
- YouTube search: https://www.youtube.com/results?search_query=ARM-Wrestling%3A+Overcoming+CPU+Migration+Challenges+to+Reduce+Costs+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hD5lXEgp9Tg
- YouTube title: ARM-Wrestling: Overcoming CPU Migration Challenges to Reduce Costs- Laurent Bernaille, Eric Mountain
- Match score: 0.882
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/arm-wrestling-overcoming-cpu-migration-challenges-to-reduce-costs/hD5lXEgp9Tg.txt
- Transcript chars: 33428
- Keywords: applications, actually, application, instance, running, images, docker, binary, course, instances, pretty, cost, migrate, little, builds, migrated, performance, better

### Resumo baseado na transcript

hello everyone uh we're very happy to be here today we're going to to to tell you how we migrated to arm at at data dog so I'm Lauren bernai and Eric is going to start hello hi yes so I'm Eric mountain and uh so data dog we're an observability monitoring and security platform and uh we we inest an awful lot of data we present that data to our users and to run all these Services we need need a lot of infrastructure tens of thousands of hosts

### Excerpt da transcript

hello everyone uh we're very happy to be here today we're going to to to tell you how we migrated to arm at at data dog so I'm Lauren bernai and Eric is going to start hello hi yes so I'm Eric mountain and uh so data dog we're an observability monitoring and security platform and uh we we inest an awful lot of data we present that data to our users and to run all these Services we need need a lot of infrastructure tens of thousands of hosts running on dozens of kubernetes service uh clusters this uh costs a lot of money so we're of course introducing and minimizing our costs so today we're here to tell you a bit about well why did we want to migrate to arm uh how we bootstrapped that initiative how we then scale the migration once we got past the first few applications uh running in production on arm and what's our strategy to today now that we've got a lot of applications running on arm what do we want to do um so why arm anyway for a start so the game changer was in 2019 when AWS announced the graviton 2 based instances because these were the first ones to actually be somewhere on par with C5 M5 uh type instances that are the kinds that we use typically for most of our workloads so there these gravit twos seemed capable of of running our workloads and synthetic benchmarks that you can find like on fonics uh seem to indicate that indeed performance was good and even possibly better than the the x86 based uh offering um also these new instance types were actually 20% cheaper than the hardware equivalent uh C5 M5 R5 uh instances so it seemed on paper a very good offering um to re assure ourselves a little bit we also did some internal benchmarks on a few uh applications that we use a lot so etcd redis kfka uh here we got a few results for Fred City and we're seeing basically that it's actually 25% faster on top of being 20% cheaper for some real work loans not just synthetic benchmarks so this was rather comforting um at the executive level uh our CTO Alex he wanted us to he gave us the mission to go out and try and migrate workloads to are uh to control our costs uh we want to control our costs and if we can get certain percentage out from just migrating to arm well that's already a benefit um the arm footprint is growing fast we see AWS with new instance types Apple was uh driving their own Apple silicon already at the time uh so the ecosystem is maturing uh we thought that most of the effort would be on platform teams like compute and builds c those kind
