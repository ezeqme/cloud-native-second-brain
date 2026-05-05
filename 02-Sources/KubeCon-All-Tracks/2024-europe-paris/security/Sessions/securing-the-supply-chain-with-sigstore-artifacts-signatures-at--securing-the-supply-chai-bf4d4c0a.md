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
themes: ["AI ML", "Security", "SRE Reliability"]
speakers: ["Dmitry Savintsev", "Yonghe Zhao", "Yahoo"]
sched_url: https://kccnceu2024.sched.com/event/1YeNE/securing-the-supply-chain-with-sigstore-artifacts-signatures-at-scale-dmitry-savintsev-yonghe-zhao-yahoo
youtube_search_url: https://www.youtube.com/results?search_query=Securing+the+Supply+Chain+with+Sigstore+Artifacts+Signatures+at+Scale+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Securing the Supply Chain with Sigstore Artifacts Signatures at Scale - Dmitry Savintsev & Yonghe Zhao, Yahoo

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Dmitry Savintsev, Yonghe Zhao, Yahoo
- Schedule: https://kccnceu2024.sched.com/event/1YeNE/securing-the-supply-chain-with-sigstore-artifacts-signatures-at-scale-dmitry-savintsev-yonghe-zhao-yahoo
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+the+Supply+Chain+with+Sigstore+Artifacts+Signatures+at+Scale+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Securing the Supply Chain with Sigstore Artifacts Signatures at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNE/securing-the-supply-chain-with-sigstore-artifacts-signatures-at-scale-dmitry-savintsev-yonghe-zhao-yahoo
- YouTube search: https://www.youtube.com/results?search_query=Securing+the+Supply+Chain+with+Sigstore+Artifacts+Signatures+at+Scale+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Tp-t_7ccW0Y
- YouTube title: Securing the Supply Chain with Sigstore Artifacts Signatures at Scale
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/securing-the-supply-chain-with-sigstore-artifacts-signatures-at-scale/Tp-t_7ccW0Y.txt
- Transcript chars: 25171
- Keywords: signing, security, verification, signature, certificate, signatures, images, private, authority, record, registry, public, verify, software, signed, started, digital, source

### Resumo baseado na transcript

hello Salu welcome and thanks to coming our session securing the supply chain with six store artifact signatures at scale I'm Dimitri sain an engineer at Yahoo security team working on the companywide security infrastructure uh I'm Yung I also work for the Yahoo security team our security team is known as the paranoid and as the top of the slices are uh logo uh we are very excited to be here the topic we are going to talk about is something that concerns all the kubernetes users kubernetes has

### Excerpt da transcript

hello Salu welcome and thanks to coming our session securing the supply chain with six store artifact signatures at scale I'm Dimitri sain an engineer at Yahoo security team working on the companywide security infrastructure uh I'm Yung I also work for the Yahoo security team our security team is known as the paranoid and as the top of the slices are uh logo uh we are very excited to be here the topic we are going to talk about is something that concerns all the kubernetes users kubernetes has lots of moving parts and infrastructure but in the end it's about Parts running containers that do the useful work and these containers are started off oci or DOA images the big question is how do we know how can we be sure and how to verify that those images are really the ones that we intend to run and not some malicious falsification and also how to do such verification for all of possibly millions of images we are deploying in this talk we want to share what we have done trying to answer those questions and here's the agenda supply chain security is about tracing the things we use from their region and throughout their existence it may be best to illustrate the dangers and risks with a couple of horror stories how things can go terribly wrong in this area supply chain security concerns not only software a literally deadly example is the case with stylenl poisonings when the capsules laced with C were placed on the store shelves as a reaction to this the company Johnson and Johnson introduced temper evident packaging for all its over-the-counter medications and they were able to overcome the crisis and win back the users trust in the software area the solar winds attack isn't famous hackers compromised the software update mechanism and new versions of the popular oron Network management software brought militia code to government agencies and major corporations one more example the Cod cough incident Intruders were able to modify the bash uploader script and that resulted in compromise of code and credentials of code cough users in their C CI setup and that went undetected for a couple of months the software supply chain attacks exploit the time gap between the generation of software artifact and its usage the generation can be for example an oci image built in a CI pipeline which is then stored in a registry potentially for a very long time and its consumption would be deployment in a kubernetes clusters this time the intermediate time of storage can be between s
