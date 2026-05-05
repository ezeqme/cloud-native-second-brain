---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Cloud Native Novice"
themes: ["Security"]
speakers: ["Andrew Davis", "Independent", "Sandeep Kanabar", "Gen (formerly NortonLifeLock)"]
sched_url: https://kccncna2024.sched.com/event/1i7ob/tls-and-mtls-introduction-to-modern-security-andrew-davis-independent-sandeep-kanabar-gen-formerly-nortonlifelock
youtube_search_url: https://www.youtube.com/results?search_query=TLS+and+MTLS%3A+Introduction+to+Modern+Security+CNCF+KubeCon+2024
slides: []
status: parsed
---

# TLS and MTLS: Introduction to Modern Security - Andrew Davis, Independent & Sandeep Kanabar, Gen (formerly NortonLifeLock)

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Security]]
- País/cidade: United States / Salt Lake City
- Speakers: Andrew Davis, Independent, Sandeep Kanabar, Gen (formerly NortonLifeLock)
- Schedule: https://kccncna2024.sched.com/event/1i7ob/tls-and-mtls-introduction-to-modern-security-andrew-davis-independent-sandeep-kanabar-gen-formerly-nortonlifelock
- Busca YouTube: https://www.youtube.com/results?search_query=TLS+and+MTLS%3A+Introduction+to+Modern+Security+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre TLS and MTLS: Introduction to Modern Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ob/tls-and-mtls-introduction-to-modern-security-andrew-davis-independent-sandeep-kanabar-gen-formerly-nortonlifelock
- YouTube search: https://www.youtube.com/results?search_query=TLS+and+MTLS%3A+Introduction+to+Modern+Security+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=N2x58qHHtiM
- YouTube title: TLS and MTLS: Introduction to Modern Security - Andrew Davis & Sandeep Kanabar
- Match score: 0.832
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tls-and-mtls-introduction-to-modern-security/N2x58qHHtiM.txt
- Transcript chars: 19535
- Keywords: certificate, communication, secure, cryptography, identity, security, server, public, verify, encryption, client, critical, systems, authentication, trusted, protocols, private, exchange

### Resumo baseado na transcript

hello everyone hello and welcome it's good to be here right so let's go ahead and get started my name is Andrew Davis and I'm a cyber security expert and I am currently a member of the deaa and heart of hearing working group with cncf it is my pleasure to be here with you at cubec con and I'm sand canabar a Le software engineer at Jin who are excited to walk you to one of the most fundamental yet misunderstood Technologies in security TLS and mtls we will

### Excerpt da transcript

hello everyone hello and welcome it's good to be here right so let's go ahead and get started my name is Andrew Davis and I'm a cyber security expert and I am currently a member of the deaa and heart of hearing working group with cncf it is my pleasure to be here with you at cubec con and I'm sand canabar a Le software engineer at Jin who are excited to walk you to one of the most fundamental yet misunderstood Technologies in security TLS and mtls we will break down what these protocols do while they are critical for secure communication and how they apply especially in the zuro trust model and before we dive into the technical aspect we would like to highlight that we both are members of the death and hard of hearing working group and so while you seeing that Andrew is using an interpreter okay I'm using the capss on my phone to follow what Android interpreter is speaking so if you see me looking at the phone in the middle of my talk I'm not read in my company emails okay okay so so now imagine a world where every conversation every communication every digital thing could be EES dropped on or tampered with this is the reality before the Advent of cryptography and secure communication protocols like TLS and mtls these Technologies are the foundation of modern security ensuring that confidentiality integrity and authenticity of our digital Communications TLS and mtls are the unsung heroes of modern security they're like the Bodyguards of the digital world protecting our sensitive information from prying eyes and malicious attacks but like any bodyguard they need to be used correctly unfortunately many people don't understand these Technologies which can lead to security vulnerabilities and that's why we're here today we're going to take a deep dive into TLS and mtls uncovering their secrets and learning how to use them to their full potential so let's go over today's agenda we're going to start with why we need TLS and mtls we are going to discuss basics of security and cryptography we are going to talk about public key cryptography and infrastructure the next item will be TLS mtls and zero trust and finally we'll talk about a practical example service meeses specifically using Linker so let's start with a critical question why do we need secure communication the answer might seem obvious but understanding the specific threats helps us understand how we can address them first consider eavesdropping without secure communication any data transmitted over a ne
