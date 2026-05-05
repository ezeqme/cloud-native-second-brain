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
themes: ["AI ML", "Security"]
speakers: ["Steve Lasker", "Microsoft"]
sched_url: https://kccnceu2022.sched.com/event/ytpZ/distributing-supply-chain-artifacts-with-oci-oras-artifacts-steve-lasker-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Distributing+Supply+Chain+Artifacts+with+OCI+%26+ORAS+Artifacts+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Distributing Supply Chain Artifacts with OCI & ORAS Artifacts - Steve Lasker, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: Spain / Valencia
- Speakers: Steve Lasker, Microsoft
- Schedule: https://kccnceu2022.sched.com/event/ytpZ/distributing-supply-chain-artifacts-with-oci-oras-artifacts-steve-lasker-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Distributing+Supply+Chain+Artifacts+with+OCI+%26+ORAS+Artifacts+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Distributing Supply Chain Artifacts with OCI & ORAS Artifacts.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytpZ/distributing-supply-chain-artifacts-with-oci-oras-artifacts-steve-lasker-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Distributing+Supply+Chain+Artifacts+with+OCI+%26+ORAS+Artifacts+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lT2ZMRJrQsU
- YouTube title: Distributing Supply Chain Artifacts with OCI & ORAS Artifacts - Steve Lasker, Microsoft
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/distributing-supply-chain-artifacts-with-oci-oras-artifacts/lT2ZMRJrQsU.txt
- Transcript chars: 34577
- Keywords: registry, software, manifest, monitor, artifacts, little, storage, actually, registries, content, information, version, s-bomb, deployed, another, available, already, artifact

### Resumo baseado na transcript

well hello everybody it's getting towards the end of the week hopefully everybody's starting to think about how they're going to enjoy wonderful valencia so i'm here to talk about distributing supply chain artifacts anybody thinking about security these days right kind of a little bit of a focus um there's lots of new supply chain artifacts where are we going to store them how are you going to handle them what do we do with these things so i'm steve lasker i'm a pm architect in azure and this

### Excerpt da transcript

well hello everybody it's getting towards the end of the week hopefully everybody's starting to think about how they're going to enjoy wonderful valencia so i'm here to talk about distributing supply chain artifacts anybody thinking about security these days right kind of a little bit of a focus um there's lots of new supply chain artifacts where are we going to store them how are you going to handle them what do we do with these things so i'm steve lasker i'm a pm architect in azure and this is an area that i've been spending a lot of time thinking about for how we store and distribute them and something we've been working on for a while actually so i'll kind of talk about what we've been thinking about and how it's been evolving so lots of supply chain artifacts where are you going to store them how are you going to distribute them it turns out the what matters because of some of the best practices for how we think about just to distribute and deploy these and we'll talk a little bit about should we be building new services or should we invest and extend some of the existing services that you're all using already so i'll spend a little time talking about this elegance and evolution of registries which will put context to the whole whole thing of oci and aura's artifacts so there's lots of them oh my it's just every day there's a new artifact type that's coming out whether it's a new s-bomb format or claims or attestations there's just lots of different types that are applying to the software already thinking about so we think about containers but there's packages there's loose binaries turns out there's iot deployments that we should be thinking about from the killer cars that can be taken over to the medical devices that are in the people that got hit by the killer cars right these are all components that we should be thinking about of how do we have supply chain artifacts around these new types or new types around the existing things we're already deploying but it also applies to our vms that are under the covers for all of our containers that we're running right this is not a new problem it's just a matter of how do we think about it across the spectrum of software and hardware quite frankly so as we started this effort several years ago a lot of these formats didn't exist they continue to pop up so how can we think about associating all of those with the type of software we're building so where will you store them does it matter do you need to distri
