---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Yi Zha", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcut/project-lightning-talk-notary-project-securing-binary-artifacts-with-fine-grained-control-yi-zha-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Notary+Project%3A+Securing+Binary+Artifacts+with+Fine-grained+Control+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Notary Project: Securing Binary Artifacts with Fine-grained Control - Yi Zha, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Yi Zha, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcut/project-lightning-talk-notary-project-securing-binary-artifacts-with-fine-grained-control-yi-zha-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Notary+Project%3A+Securing+Binary+Artifacts+with+Fine-grained+Control+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Notary Project: Securing Binary Artifacts with Fine-grained Control.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcut/project-lightning-talk-notary-project-securing-binary-artifacts-with-fine-grained-control-yi-zha-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Notary+Project%3A+Securing+Binary+Artifacts+with+Fine-grained+Control+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dT-ShZYM3SI
- YouTube title: Project Lightning Talk: Notary Project: Securing Binary Artifacts with Fine-grained Control - Yi Zha
- Match score: 1.042
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-notary-project-securing-binary-artifacts-with-f/dT-ShZYM3SI.txt
- Transcript chars: 4446
- Keywords: images, artifacts, notary, signature, ensure, policy, notation, vulnerability, arbitrary, docker, software, trusted, source, standard, solutions, support, create, verify

### Resumo baseado na transcript

Okay, in today's talk I will talk about uh uh notary project a short overview and also our new feature sign arbitary profiles. So not project it's a sense of incubating project and in today's uh software world so the cyber attack on the securing uh sub attack on the software supply chain is quite frequent and cause severe impact. So uh if you want to learn more about not project and you want to see a demo so feel free to join uh maintenance track on the uh I think in the last day uh in the afternoon of the last day Friday and we also have a project uh kiosk uh since tomorrow.

### Excerpt da transcript

Hello everyone. Uh my name is E. I'm currently the notary project maintainer. So how many of you know notary project? Okay. How many of you sign container images? Okay. Looks good. How many of you use images from Docker Hub directory? Okay, cool. Okay, in today's talk I will talk about uh uh notary project a short overview and also our new feature sign arbitary profiles. So not project it's a sense of incubating project and in today's uh software world so the cyber attack on the securing uh sub attack on the software supply chain is quite frequent and cause severe impact. So developers also uh frequently ask questions. How can I ensure artifacts that I use are from trusted source and how can I ensure those artifacts are not altered uh since creation. So notary project answer these questions by providing standard based solutions and tools. So uh we complied with the OCI artifact OCI specification the latest 1.1 so that you can manage the signature in the OCI compliant regry efficiently and we also support two ITF standard based signature format one is JSON formatted uh JWS another is uh uh binary encoded coy signatures and not project also create addition specifications so that you can build your own uh reference implementation based on your need and this is quite important especially for much uh cloud environment.

This can ensure the uh interoperability and compability by uh using the standard based solutions. And currently we have a major cloud vendor uh adopt the not project solutions and the tools and also some popular open source projects. So how or when do I uh use not projects? So this is one typic uh scenario. uh it is to ensure the uh authenticity and integrity uh of OSI images throughout its life cycle. So um so when you acquire images from for example Docker harp you need to verify the signature to ensure they are from trusted source right. So after you acquire those docker images and you want your internal team to use that you put into a catalog registry. So normally you will do vulnerability scanning and generate the vulnerability reports and for some cases you even patch those images before the upstream has that uh uh new version ready. So for those new patched images or uh vulnerability reports you can use not project to sign it find sign them and during the build before you use for example base images for build your own application images you can wify the signature to ensure the base images are trusted and approved uh of use by your organiz
