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
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1bK6A/security-hub-unconference-demo-archivista-using-tuf-to-store-policy-building-trust-on-verifying-in-toto-attestations
youtube_search_url: https://www.youtube.com/results?search_query=SECURITY+HUB+%7C+Unconference%3A+DEMO%3A+Archivista+using+TUF+to+store+Policy+%26+building+trust+on+verifying+in-toto+Attestations+CNCF+KubeCon+2024
slides: []
status: parsed
---

# SECURITY HUB | Unconference: DEMO: Archivista using TUF to store Policy & building trust on verifying in-toto Attestations

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1bK6A/security-hub-unconference-demo-archivista-using-tuf-to-store-policy-building-trust-on-verifying-in-toto-attestations
- Busca YouTube: https://www.youtube.com/results?search_query=SECURITY+HUB+%7C+Unconference%3A+DEMO%3A+Archivista+using+TUF+to+store+Policy+%26+building+trust+on+verifying+in-toto+Attestations+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre SECURITY HUB | Unconference: DEMO: Archivista using TUF to store Policy & building trust on verifying in-toto Attestations.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1bK6A/security-hub-unconference-demo-archivista-using-tuf-to-store-policy-building-trust-on-verifying-in-toto-attestations
- YouTube search: https://www.youtube.com/results?search_query=SECURITY+HUB+%7C+Unconference%3A+DEMO%3A+Archivista+using+TUF+to+store+Policy+%26+building+trust+on+verifying+in-toto+Attestations+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=camLVqnVel8
- YouTube title: SECURITY HUB | Unconference: DEMO: Archivista using TUF to store Policy & buildin... Kairo de Araujo
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/security-hub-unconference-demo-archivista-using-tuf-to-store-policy-bu/camLVqnVel8.txt
- Transcript chars: 16463
- Keywords: metadata, policy, attestation, attestations, witness, version, generate, validate, artifact, second, basically, information, verify, everything, signed, create, archist, policies

### Resumo baseado na transcript

okay uh yeah sorry for thank you for so yeah well what uh I will share here today it's about uh the archist storying Polish and using tough to build trust maybe nobody is familiar with many of those words here but I will try to give a little introduction before we start so my name is Kyo I work uh at testify secc I'm an open source engineer I'm author of The repository as for tough It's one um service that provides the tough uh repository I'm also maintaining

### Excerpt da transcript

okay uh yeah sorry for thank you for so yeah well what uh I will share here today it's about uh the archist storying Polish and using tough to build trust maybe nobody is familiar with many of those words here but I will try to give a little introduction before we start so my name is Kyo I work uh at testify secc I'm an open source engineer I'm author of The repository as for tough It's one um service that provides the tough uh repository I'm also maintaining the in Arch Vista and I'm active in the tough community and I will advise for everyone if there is more advanced T questions there are many people there that can answer that but let's uh okay first uh I just prepare this quick introduction here uh D too is an attestation framework um and we'll talk about witness here witness is uh using a the Toto uh framework to and this is an CLI uh that um allows you to uh generate attestations and also verify this uh polic uh this attestations against uh policies so I will talk I will demo what I will demo here we use uh we need to generate an attestation and validate the PO um archiv Vista it's a graph and the storage serves for in attestations it means that if you generate attestations you can store all the attestations in Arista you have graph C to make queries so you can retrieve the testation that you want to verify excuse me and um tough is a framework to secure the distribution of artifacts and doesn't matter which it's your artifact actually uh of course we use this a lot for software but any kind of document uh uh imag what you need uh you can use and in that demo I will be using also our stuff um because this I don't need to build in archist all the tough repository so I can just integrate it with AR stuff um okay what I will demo here will be basically this confusing diagram of course we go for part I will divide it in parts to make uh more understandable yeah what we show here is the process um of witness generating an ation and storing this attestation in Arista and this attestation will be available for queres for witness when they want to verify what is in below here uh of course uh we sh I will show also the um the policy uh generation uh and the storing this policy in the archiv Vista so what I need to uh also highlight here is that that currently uh witness and Arista can store an attestation but cannot store a polic so what I will demo here is actually on work in progress uh it's a a PC of arivis histor policy also currently Arisa doesn't suppor
