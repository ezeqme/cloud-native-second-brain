---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Service Mesh"
themes: ["Security", "Networking"]
speakers: ["Liz Rice", "Isovalent"]
sched_url: https://kccncna2023.sched.com/event/1R2tD/when-is-a-secure-connection-not-encrypted-and-other-stories-liz-rice-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=When+Is+a+Secure+Connection+Not+Encrypted%3F+and+Other+Stories+CNCF+KubeCon+2023
slides: []
status: parsed
---

# When Is a Secure Connection Not Encrypted? and Other Stories - Liz Rice, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Security]], [[Networking]]
- País/cidade: United States / Chicago
- Speakers: Liz Rice, Isovalent
- Schedule: https://kccncna2023.sched.com/event/1R2tD/when-is-a-secure-connection-not-encrypted-and-other-stories-liz-rice-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=When+Is+a+Secure+Connection+Not+Encrypted%3F+and+Other+Stories+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre When Is a Secure Connection Not Encrypted? and Other Stories.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2tD/when-is-a-secure-connection-not-encrypted-and-other-stories-liz-rice-isovalent
- YouTube search: https://www.youtube.com/results?search_query=When+Is+a+Secure+Connection+Not+Encrypted%3F+and+Other+Stories+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5U9h4E0H5RA
- YouTube title: When Is a Secure Connection Not Encrypted? and Other Stories - Liz Rice, Isovalent
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/when-is-a-secure-connection-not-encrypted-and-other-stories/5U9h4E0H5RA.txt
- Transcript chars: 25875
- Keywords: identity, traffic, policy, encryption, security, authentication, running, address, handshake, connection, encrypted, labels, network, spiffy, workloads, interface, question, secure

### Resumo baseado na transcript

hi and thank you for coming to my talk about when a secure connection might not be encrypted and a few other stories my name is Liz rice I work at a company called ISO veent which is the company that originally created the selum project how many of you have heard of celum excellent hopefully you all know that celum recently graduated in the cncf so that's really exciting for us and uh frankly I think deserves a round of applause thank you and today I want to talk worked right and we know Darth Vader doesn't have any labels because it's he not in the kubernetes world so instead what I'm going to do is instead of matching on labels I'm going to say all entities are allowed to communicate provided they can

### Excerpt da transcript

hi and thank you for coming to my talk about when a secure connection might not be encrypted and a few other stories my name is Liz rice I work at a company called ISO veent which is the company that originally created the selum project how many of you have heard of celum excellent hopefully you all know that celum recently graduated in the cncf so that's really exciting for us and uh frankly I think deserves a round of applause thank you and today I want to talk about a beta feature that's in uh recent versions of syum for Mutual authentication and let's take a step back and talk about what we mean when we say a connection is secure and I think one of the best ways to think about this is to think about what you want when you're talking to your bank over the internet you absolutely need to authenticate identities you need to know you need the bank to know that you're you because you don't want to be paying money into somebody else's account you want to know that you're talking to the bank because you don't want to be paying your money into some random person so that establishment of both ends of uh or the identity at both ends of a connection is critical it's also important to then encrypt the traffic that's flowing between those end points because you don't want everybody knowing how much money you've got in your bank account uh and you also don't want them potentially monitoring that traffic to for example get your password in the environment where we're talking about a web browser talking to a bank we're probably talking about TLS I'm sure you're all familiar with the little padlock icon that you get in the browser when TLS has been established we don't need to go through all all the details of how that TLS handshake happens but the core parts are it starts with a TCP connection so there's a a client end that initiates a TCP connection that sinac flow is the beginning of every TCP communication and then the client initiates this handshake asking the server for its identity in the form of an x509 certificate so this is the bit that proves that the bank is really the bank the client can validate that certificate and proceed there's also some exchange of information that allows both ends to derive uh key that they can use for encrypting traffic for the duration of that session in a cloud native environment we typically talk about Mutual TLS between two workloads when you're talking to your bank you probably do TLS to establish that it's the bank and then y
