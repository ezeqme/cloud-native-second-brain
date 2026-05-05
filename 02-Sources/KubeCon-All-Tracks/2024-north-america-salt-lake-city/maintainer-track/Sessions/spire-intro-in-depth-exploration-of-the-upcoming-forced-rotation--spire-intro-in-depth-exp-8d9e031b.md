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
themes: ["AI ML", "Community Governance"]
speakers: ["Agustín Martínez Fayó", "Marcos Yacob", "Hewlett Packard Enterprise"]
sched_url: https://kccncna2024.sched.com/event/1howH/spire-intro-in-depth-exploration-of-the-upcoming-forced-rotation-and-revocation-feature-agustin-martinez-fayo-marcos-yacob-hewlett-packard-enterprise
youtube_search_url: https://www.youtube.com/results?search_query=SPIRE%3A+Intro+%26+In-Depth+Exploration+of+the+Upcoming+Forced+Rotation+and+Revocation+Feature+CNCF+KubeCon+2024
slides: []
status: parsed
---

# SPIRE: Intro & In-Depth Exploration of the Upcoming Forced Rotation and Revocation Feature - Agustín Martínez Fayó & Marcos Yacob, Hewlett Packard Enterprise

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Agustín Martínez Fayó, Marcos Yacob, Hewlett Packard Enterprise
- Schedule: https://kccncna2024.sched.com/event/1howH/spire-intro-in-depth-exploration-of-the-upcoming-forced-rotation-and-revocation-feature-agustin-martinez-fayo-marcos-yacob-hewlett-packard-enterprise
- Busca YouTube: https://www.youtube.com/results?search_query=SPIRE%3A+Intro+%26+In-Depth+Exploration+of+the+Upcoming+Forced+Rotation+and+Revocation+Feature+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre SPIRE: Intro & In-Depth Exploration of the Upcoming Forced Rotation and Revocation Feature.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1howH/spire-intro-in-depth-exploration-of-the-upcoming-forced-rotation-and-revocation-feature-agustin-martinez-fayo-marcos-yacob-hewlett-packard-enterprise
- YouTube search: https://www.youtube.com/results?search_query=SPIRE%3A+Intro+%26+In-Depth+Exploration+of+the+Upcoming+Forced+Rotation+and+Revocation+Feature+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VWmBc1mexYo
- YouTube title: SPIRE: Intro & In-Depth Exploration of the Upcoming Forced Rotation and Revoc... A.M. Fayó, M. Yacob
- Match score: 0.961
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/spire-intro-in-depth-exploration-of-the-upcoming-forced-rotation-and-r/VWmBc1mexYo.txt
- Transcript chars: 18458
- Keywords: authority, active, rotation, server, prepare, signing, bundle, authorities, client, pretty, defines, current, happen, basically, reason, workload, important, activate

### Resumo baseado na transcript

my name is atin Martino I am a maintainer of the Spire project I'm here with Marcos hello I'm maros another of the maintainers we are going to present this okay so uh either if you are new to Spire or if you want to learn about the new Force rotation or and revocation feature I hope uh that you find this presentation interesting um so we will provide a very quick uh introduction um to spify and spire and then we will get into the details of the uh

### Excerpt da transcript

my name is atin Martino I am a maintainer of the Spire project I'm here with Marcos hello I'm maros another of the maintainers we are going to present this okay so uh either if you are new to Spire or if you want to learn about the new Force rotation or and revocation feature I hope uh that you find this presentation interesting um so we will provide a very quick uh introduction um to spify and spire and then we will get into the details of the uh new support for Force rotation and revocation um to do that we will uh look at um the different signing Keys uh that Spire Spire can handle um what's the normal like cycle of the signing keys and how you can now Force the rotation of the keys and finally we will have a live demo of how of all this work okay so let's let's do a very very quick overview of spify uh we need to talk about the spify before talking about Spire um spify essentially defines a framework uh and a set of Standards um to identify and secure Communications between workflows um in order to do that um it defines a few things uh first it defines how Services identify themselves to each other to do that um it defines uh a form for the IDS and that's what we call the spey IDS um but also you need uh a some kind of document where you can put those IDs and for that it uh defines the spify verifiable identity documents where the spify IDS are encoded once you have that um you also need a way to dist distribute um the svits um and for that it defines what we call the workload API that's uh an API specification that uh defines the issuance and retriving the S bits um and finally you also need uh a way to verify if an SVD is valid in a trust domain and for that it defines what we call a trust bundle so it um defines the format for representing what's the the collection of the public keys that are in use in a given uh spey Authority um in addition to that it also specifies how you can Federate with other trust domain and how you can establish trust with other trust domains so all all that is about um spe very quickly now that we know about spy we can start start talking about Spire um an Spire is an implementation of the SP standards that performs node and workload attestation and for that it has two measure component that are the server and the asent the server is the one that authenticate agents and me s s bits and the agent uh primarily um serve the spify workload API that's the API that the workloads use to retrive their identities okay so let get in
