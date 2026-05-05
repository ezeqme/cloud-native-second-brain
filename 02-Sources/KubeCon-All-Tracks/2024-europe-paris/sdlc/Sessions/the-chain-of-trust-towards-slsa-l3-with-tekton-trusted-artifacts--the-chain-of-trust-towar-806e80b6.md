---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "SDLC"
themes: ["AI ML"]
speakers: ["Jerop Kipruto", "Google", "Andrea Frittoli", "IBM"]
sched_url: https://kccnceu2024.sched.com/event/1YeNY/the-chain-of-trust-towards-slsa-l3-with-tekton-trusted-artifacts-jerop-kipruto-google-andrea-frittoli-ibm
youtube_search_url: https://www.youtube.com/results?search_query=The+Chain+of+Trust%3A+Towards+SLSA+L3+with+Tekton+Trusted+Artifacts+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The Chain of Trust: Towards SLSA L3 with Tekton Trusted Artifacts - Jerop Kipruto, Google & Andrea Frittoli, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[SDLC]]
- Temas: [[AI ML]]
- País/cidade: France / Paris
- Speakers: Jerop Kipruto, Google, Andrea Frittoli, IBM
- Schedule: https://kccnceu2024.sched.com/event/1YeNY/the-chain-of-trust-towards-slsa-l3-with-tekton-trusted-artifacts-jerop-kipruto-google-andrea-frittoli-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=The+Chain+of+Trust%3A+Towards+SLSA+L3+with+Tekton+Trusted+Artifacts+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The Chain of Trust: Towards SLSA L3 with Tekton Trusted Artifacts.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNY/the-chain-of-trust-towards-slsa-l3-with-tekton-trusted-artifacts-jerop-kipruto-google-andrea-frittoli-ibm
- YouTube search: https://www.youtube.com/results?search_query=The+Chain+of+Trust%3A+Towards+SLSA+L3+with+Tekton+Trusted+Artifacts+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jaC9eVEcwzk
- YouTube title: The Chain of Trust: Towards SLSA L3 with Tekton Trusted Artifacts - Jerop Kipruto & Andrea Frittoli
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-chain-of-trust-towards-slsa-l3-with-tekton-trusted-artifacts/jaC9eVEcwzk.txt
- Transcript chars: 28826
- Keywords: pipeline, tecton, artifacts, artifact, actually, software, workspace, produced, resources, producer, consumer, produce, provenance, events, attestation, status, introduce, information

### Resumo baseado na transcript

all right uh let's get started hello everyone and welcome to the chain of trust toward salsa elree with techon trusted artifact so thanks for joining today uh unfortunately uh my colleague jro couldn't travel today to the conference so it will be just me delivering uh the presentation today uh thanks for joining um I know it's one of the last sessions of the day uh hopefully it will be uh interesting and exciting uh so my name is Andrea frto um I'm an open source developer advocat work

### Excerpt da transcript

all right uh let's get started hello everyone and welcome to the chain of trust toward salsa elree with techon trusted artifact so thanks for joining today uh unfortunately uh my colleague jro couldn't travel today to the conference so it will be just me delivering uh the presentation today uh thanks for joining um I know it's one of the last sessions of the day uh hopefully it will be uh interesting and exciting uh so my name is Andrea frto um I'm an open source developer advocat work for IBM I'm the chair of the TOC for the continuous delivery Foundation that's a sister Foundation to the cncf and we focus on uh cicd and I'm also a maintainer of the tecton project and member of the governing board there and jerro who couldn't be here uh today she's a senior software engineer at Google and she's also techon maintainer and member of the governing board so today we'll start talking about chain of trust in the soft development life life cycle uh context I'll introduce uh tecton and talk about it um then we'll talk about artifacts for tecton and have a short demo about it and finally we discuss what's next what the future brings in this context but let's start with a chain of trust I mean I probably don't need to speak spend too many words about software development life cycle as this is the sdlc track um but yeah when thinking about software and software being produced we usually start from a producer which is typically is a developer or team of developers writing the softare as everyone is talking about AI could be maybe some AI system contributing to it and then the software goes through a series of steps typically it's stored in a software um configuration management system then goes for a build process which might bring in a certain number of dependencies the result is packaged and then the package is what gets the final consumer and so a chain of trust in this context it means that we can put a certain level of Trust on every single step in this process that I've just just described so in all the processes that we have in our uh software development life cycle and uh each one of them so at the end the consumer can trust that what it's consuming what it's using either as a dependency or an application is actually what was in the intended result by the producer uh but what happens is something goes wrong is enough that one uh part of the chain is broken and then the chain of trust Falls and so this picture is taken from the salsa specification I will talk
