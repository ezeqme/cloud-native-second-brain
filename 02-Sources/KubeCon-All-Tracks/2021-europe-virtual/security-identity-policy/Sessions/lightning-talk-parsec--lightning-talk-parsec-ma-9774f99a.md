---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Security + Identity + Policy"
themes: ["Security"]
speakers: ["Marc Meunier", "Arm"]
sched_url: https://kccnceu2021.sched.com/event/j3Vq/lightning-talk-parsec-marc-meunier-arm
youtube_search_url: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Parsec+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Lightning Talk: Parsec - Marc Meunier, Arm

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: Virtual / Virtual
- Speakers: Marc Meunier, Arm
- Schedule: https://kccnceu2021.sched.com/event/j3Vq/lightning-talk-parsec-marc-meunier-arm
- Busca YouTube: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Parsec+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Lightning Talk: Parsec.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/j3Vq/lightning-talk-parsec-marc-meunier-arm
- YouTube search: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Parsec+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=G-MvFqkVJTI
- YouTube title: Lightning Talk: Parsec - Marc Meunier, Arm
- Match score: 0.792
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/lightning-talk-parsec/G-MvFqkVJTI.txt
- Transcript chars: 6312
- Keywords: parsec, security, application, interface, projects, provides, functions, implement, implemented, provider, multiple, abstraction, router, applications, without, hardware, module, simple

### Resumo baseado na transcript

hello everyone my name is mark marinier and i work for arm and part of the infrastructure line of business focused on software ecosystem development with a special interest in security projects so i basically work with partners to promote security advancements at the edge and in the cloud and i represent arm at the board of governance at the confidential compute consortium today i'm going to talk to you about a cncf project called parsec if you're not familiar with the cncf structure a sandbox project is an early

### Excerpt da transcript

hello everyone my name is mark marinier and i work for arm and part of the infrastructure line of business focused on software ecosystem development with a special interest in security projects so i basically work with partners to promote security advancements at the edge and in the cloud and i represent arm at the board of governance at the confidential compute consortium today i'm going to talk to you about a cncf project called parsec if you're not familiar with the cncf structure a sandbox project is an early stage project and in the case of parsec it's a new project that fits the cncf mission it was contributed to the cncf to remove possible legal and government governance obstacles to adoption and to facilitate contribution by other developers in the community it's a great place to collaborate openly on interesting projects that benefit multiple environments our goal with parsec is to mature the program and to move it up to the next level of maturity within the cncf now getting back to parsing parsec is a security project that provides an abstraction layer between router trust and applications this abstraction layer provides a set of apis for security functions such as key management or cryptographic operations provides this api to the application layer without creating a strong dependency on the security primitives in the system let's consider an example to showcase the flexibility that parsec brings to a system for this example we'll take a raspberry pi and a need to implement a key exchange between a cloud service and the end device now as a developer you can implement this feature directly and be up and running fairly quickly but then what happens if you need to harden your solution and protect the keys in a hardware distrust like a tpm at this point you might decide that it's easier to code to the new security interface to start over from scratch and re-implement the security functions tied to that hardware module you'll realize that it's a lot of work and it's complicated to implement even a simple function such as key exchange with the tpm interface now consider what happens if you need to change the hardware trust with a different implementation like our hsm module if you implemented directly against the tpm interface you now need to start over once again and re-implement that security function to work with a new interface the hsm module here's where parsec comes in parsec can provide a standard interface to the application layer that doesn't
