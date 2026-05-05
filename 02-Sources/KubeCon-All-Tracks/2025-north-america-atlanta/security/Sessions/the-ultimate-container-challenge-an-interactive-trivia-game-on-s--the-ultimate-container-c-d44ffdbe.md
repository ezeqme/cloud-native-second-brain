---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Aurélie Vache", "OVHcloud", "Sherine Khoury", "Red Hat"]
sched_url: https://kccncna2025.sched.com/event/27Fez/the-ultimate-container-challenge-an-interactive-trivia-game-on-supply-chain-security-aurelie-vache-ovhcloud-sherine-khoury-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=The+Ultimate+Container+Challenge%3A+An+Interactive+Trivia+Game+on+Supply+Chain+Security+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Ultimate Container Challenge: An Interactive Trivia Game on Supply Chain Security - Aurélie Vache, OVHcloud & Sherine Khoury, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: United States / Atlanta
- Speakers: Aurélie Vache, OVHcloud, Sherine Khoury, Red Hat
- Schedule: https://kccncna2025.sched.com/event/27Fez/the-ultimate-container-challenge-an-interactive-trivia-game-on-supply-chain-security-aurelie-vache-ovhcloud-sherine-khoury-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=The+Ultimate+Container+Challenge%3A+An+Interactive+Trivia+Game+on+Supply+Chain+Security+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Ultimate Container Challenge: An Interactive Trivia Game on Supply Chain Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fez/the-ultimate-container-challenge-an-interactive-trivia-game-on-supply-chain-security-aurelie-vache-ovhcloud-sherine-khoury-red-hat
- YouTube search: https://www.youtube.com/results?search_query=The+Ultimate+Container+Challenge%3A+An+Interactive+Trivia+Game+on+Supply+Chain+Security+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=n_tkj5KmzzE
- YouTube title: The Ultimate Container Challenge: An Interactive Trivia Game on Su... Aurélie Vache & Sherine Khoury
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-ultimate-container-challenge-an-interactive-trivia-game-on-supply/n_tkj5KmzzE.txt
- Transcript chars: 17995
- Keywords: create, question, docker, vulnerabilities, cosign, registry, cluster, created, dependencies, security, little, important, inside, policy, golang, signed, signature, vulnerability

### Resumo baseado na transcript

>> Yes, because in London we presented the first edition on open container initiative and here we are back with a new quiz this time to present the supply chain. So we hope that you will uh have the chance to test your knowledge around this uh area. Look for the certificate authority that's behind it and certify that you can trust that and also look for the security scan. On quay.io IO you can find the small shield that says if an image is signed and also there's a security scan by default by CLA on Harbor you can find a green check mark whenever there's a signature and a cross a red cross uh when it's not and also you can find the sbomb details and the vulnerability scan results. So salsa it's a set of incrementally adaptable guidelines for supply chain security. love to sign the provenence attestation and to and distribute it in an into envelope and you will see in demo.

### Excerpt da transcript

and welcome to >> the ultimate kutan challenge secret chain edition. >> Yes, because in London we presented the first edition on open container initiative and here we are back with a new quiz this time to present the supply chain. So we hope that you will uh have the chance to test your knowledge around this uh area. It's going to be lots of fun and we hope that you will >> we hope and then we hope that you will also learn a few things. thanks to our demos. So without further ado, >> so I'm already I'm a developer advocate at O cloud. I'm specialized in civeies infra as code and developer experience. And you >> and I'm Shireen. I work at Red Hat. I'm working on the open shift uh distribution of Kubernetes. I'm an active community member in Marseilles, France where I live. And are you guys ready? >> Yeah. This is our QR code. If you scan it, you're going to go to our Slido quiz, right? It's going to be a white page with a blue banner for So, at the moment, just scan the QR code. While we do that, I'm going to tell you a little bit of the story of this talk.

So, Aurelia and I built an an image. It's a Golang app called the Gophers API. We built it through a CI just like everybody else. is as you can see we have a lot of bad things that could happen and we want to take this image all the way to production in a safe way. So are you ready for question number one? This is where we're going to ask you about your alias. So while you enter that I'm going to keep telling you about our story here is the representative of the dev team. Yeah. And I'm gonna be the bad guy, the security guy. I'm gonna try to be a bit tough about security. Oh, the joining. Yeah. >> All right. >> Just the tall guy. Awesome. So, is it okay for you? Yeah, >> let's go. >> Almost. >> Okay. First question is going to be about the most basic thing. Which base image are we going to use? >> Right. So, when you're choosing base images from from a public registry >> like DockerHub for example, are the images that you find there always signed and secure? Easy. It's an easy question. >> Yeah. >> This is just for you to get familiar with the app or with the website.

>> So, what do you think about that? >> Yeah. >> All right. Right. >> Let's not. >> Yeah. >> All right. So, uh >> Oh, Nick. >> Yeah. >> Okay. So, as you can imagine, you can't trust any image you find out there, right? What you should look for is signatures. And when I when I say signatures is don't just see a sign that says there's a sui
