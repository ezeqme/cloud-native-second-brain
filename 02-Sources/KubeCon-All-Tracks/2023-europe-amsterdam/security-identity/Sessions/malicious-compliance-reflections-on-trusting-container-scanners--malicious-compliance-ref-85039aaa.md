---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["AI ML", "Security", "Storage Data", "Runtime Containers"]
speakers: ["Ian Coldwater", "Independent", "Duffie Cooley", "Isovalent", "Brad Geesaman", "Ghost Security", "Rory McCune", "Datadog"]
sched_url: https://kccnceu2023.sched.com/event/1Hybu/malicious-compliance-reflections-on-trusting-container-scanners-ian-coldwater-independent-duffie-cooley-isovalent-brad-geesaman-ghost-security-rory-mccune-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Malicious+Compliance%3A+Reflections+on+Trusting+Container+Scanners+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Malicious Compliance: Reflections on Trusting Container Scanners - Ian Coldwater, Independent; Duffie Cooley, Isovalent; Brad Geesaman, Ghost Security; Rory McCune, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[AI ML]], [[Security]], [[Storage Data]], [[Runtime Containers]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ian Coldwater, Independent, Duffie Cooley, Isovalent, Brad Geesaman, Ghost Security, Rory McCune, Datadog
- Schedule: https://kccnceu2023.sched.com/event/1Hybu/malicious-compliance-reflections-on-trusting-container-scanners-ian-coldwater-independent-duffie-cooley-isovalent-brad-geesaman-ghost-security-rory-mccune-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Malicious+Compliance%3A+Reflections+on+Trusting+Container+Scanners+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Malicious Compliance: Reflections on Trusting Container Scanners.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hybu/malicious-compliance-reflections-on-trusting-container-scanners-ian-coldwater-independent-duffie-cooley-isovalent-brad-geesaman-ghost-security-rory-mccune-datadog
- YouTube search: https://www.youtube.com/results?search_query=Malicious+Compliance%3A+Reflections+on+Trusting+Container+Scanners+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9weGi0csBZM
- YouTube title: Malicious Compliance: Reflections on Trusting Container... - Coldwater, Cooley, Geesaman, McCune
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/malicious-compliance-reflections-on-trusting-container-scanners/9weGi0csBZM.txt
- Transcript chars: 30464
- Keywords: results, scanners, s-bomb, findings, docker, original, security, images, trivia, software, container, metadata, multi-stage, s-bombs, malicious, generated, looking, vulnerabilities

### Resumo baseado na transcript

we're Sig honk and this is malicious compliance Reflections on trusting container scanners if you're here for murderlicious compliance hey so are we if you're not here for malicious compliance you're in the wrong room but we're happy to see you anyway I'm Brad giesteman my pronouns are he him and I'm a staff security engineer at ghost security and I enjoy hacking cloud and kubernetes with my friends here I'm Ian Coldwater pronouns they them I'm an independent security researcher a longtime Community organizer and Sig security co-chair I

### Excerpt da transcript

we're Sig honk and this is malicious compliance Reflections on trusting container scanners if you're here for murderlicious compliance hey so are we if you're not here for malicious compliance you're in the wrong room but we're happy to see you anyway I'm Brad giesteman my pronouns are he him and I'm a staff security engineer at ghost security and I enjoy hacking cloud and kubernetes with my friends here I'm Ian Coldwater pronouns they them I'm an independent security researcher a longtime Community organizer and Sig security co-chair I love hacking weird machines and bringing people together and I'm looking for work if you're hiring hi everyone my name is Rory McKeon my programs are hihem I'm a senior security Advocate with datadog and I'd like to learn about security and write blogs hey everybody I'm Duffy Cooley I'm the field CTO at ice surveillance where I get to work on things like psyllium and tetragon and ebpf I'm excited to be here with all of you in person and I'm especially excited that we are all here finally all together on the same stage that's cool oh clickers why is that doing that one second okay I'm gonna go drive this over here so Sig honk isn't an official kubernetes Sig we're a hacker crew who have been poking at kubernetes for years and we work together to share attacker perspectives and help the whole Community level up so why are we here today we have a question for all of you real quick who here has ever heard of containers love it we had a feeling by another show of hands who here has ever used a container vulnerability scanner before wow okay great perfect so one thing you might have noticed is that governments Auditors and your security teams are asking you to scan all of your container images for vulnerabilities so they are more secure but we don't hear as much about the details and as it turns out the details are important so what do containers scanners actually do and what problems do they solve and how do container scanners work are they all the same can you always trust the results let's find out in this talk we'll be mainly covering four widely used container scanners we chose trivia gripe Docker scan and Docker Scout to test but what we'll be covering here isn't necessarily limited to those four as of April 13th of this year Docker scan is powered by sneak on the back end which we thought was interesting and a lot of people still use it so we figured we'd still include it here today so to start let's use all four of these
