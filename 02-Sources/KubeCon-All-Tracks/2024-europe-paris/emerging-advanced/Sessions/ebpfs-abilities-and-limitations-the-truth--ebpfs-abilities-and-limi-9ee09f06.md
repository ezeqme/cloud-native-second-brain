---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Emerging + Advanced"
themes: ["Emerging + Advanced"]
speakers: ["Liz Rice", "John Fastabend", "Isovalent"]
sched_url: https://kccnceu2024.sched.com/event/1YeQt/ebpfs-abilities-and-limitations-the-truth-liz-rice-john-fastabend-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=eBPF%E2%80%99s+Abilities+and+Limitations%3A+The+Truth+CNCF+KubeCon+2024
slides: []
status: parsed
---

# eBPF’s Abilities and Limitations: The Truth - Liz Rice & John Fastabend, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Emerging + Advanced]]
- País/cidade: France / Paris
- Speakers: Liz Rice, John Fastabend, Isovalent
- Schedule: https://kccnceu2024.sched.com/event/1YeQt/ebpfs-abilities-and-limitations-the-truth-liz-rice-john-fastabend-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=eBPF%E2%80%99s+Abilities+and+Limitations%3A+The+Truth+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre eBPF’s Abilities and Limitations: The Truth.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQt/ebpfs-abilities-and-limitations-the-truth-liz-rice-john-fastabend-isovalent
- YouTube search: https://www.youtube.com/results?search_query=eBPF%E2%80%99s+Abilities+and+Limitations%3A+The+Truth+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tClsqnZMN6I
- YouTube title: eBPF’s Abilities and Limitations: The Truth - Liz Rice & John Fastabend, Isovalent
- Match score: 0.787
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/ebpfs-abilities-and-limitations-the-truth/tClsqnZMN6I.txt
- Transcript chars: 29896
- Keywords: program, kernel, ebpf, verifier, instructions, interesting, memory, write, million, actually, basically, programs, running, compiler, working, complete, processing, allowed

### Resumo baseado na transcript

good morning thank you so much for coming to our session this morning just about still morning right uh I hope everybody's able to find a seat if you have got a seat next to you maybe shuffle along and and let people in uh yes so my name's Liz rice uh myself and John here do you want to say hi yeah hi my name is John fman I'm engineer night surveillance and excited to talk about BPF today I've been you know working on it for almost 10

### Excerpt da transcript

good morning thank you so much for coming to our session this morning just about still morning right uh I hope everybody's able to find a seat if you have got a seat next to you maybe shuffle along and and let people in uh yes so my name's Liz rice uh myself and John here do you want to say hi yeah hi my name is John fman I'm engineer night surveillance and excited to talk about BPF today I've been you know working on it for almost 10 years now so hopefully you guys get as excited as um as I am yeah so I mean as John says he's he works in the Kel right he is a proper expert in ebpf let's just quickly recap to make sure everybody understands what we're talking about with ebpf it allows us to run custom programs in the kernel so we can change the way the kernel behaves by loading ebpf programs there and attaching them to events why is the kernel interesting well the kernel is the part of the operating system that is involved whenever we're doing anything with Hardware so if you're accessing a file or sending receiving over a network or uh even allocating memory the Kernel's going to be involved the Kernel's also um managing the processes running on a system so it's looking after things like permissions and privileges so the kernel is involved in pretty much everything interesting with ef we can change the way that it behaves so already there are lots of really great infrastructure tools built using ebpf I mean we're both very involved in psyllium and uh cium sub project tetragon doing things like networking security observability there are also loads of other great projects out there and great products out there that are doing things in these kind of infrastructure tooling spaces but sometimes you'll hear statements that give the impression that there are limits to what you can do with ebpf so for example we've heard people saying yeah you can't really Implement like layer seven paing that's just too complex for ebpf or another thing that you'll quite often hear people saying is yeah but there are limits to what you can do with ebpf because it's not cheer and complete right so do we think those statements are true well a hint here is these things were not said by people who are working on ebpf we're going to explore these kind of statements today so I've said the term cheering completeness this is not going to be a computer science class it's not going to be like super pedantic about terminology but really what true incompleteness about is about is can we pr
