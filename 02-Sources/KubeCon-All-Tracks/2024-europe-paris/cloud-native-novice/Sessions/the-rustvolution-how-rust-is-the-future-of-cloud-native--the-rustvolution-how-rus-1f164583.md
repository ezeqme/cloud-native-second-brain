---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Cloud Native Novice"
themes: ["Cloud Native Novice"]
speakers: ["Flynn", "Buoyant"]
sched_url: https://kccnceu2024.sched.com/event/1YeOy/the-rustvolution-how-rust-is-the-future-of-cloud-native-flynn-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=The+Rustvolution%3A+How+Rust+Is+the+Future+of+Cloud+Native+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The Rustvolution: How Rust Is the Future of Cloud Native - Flynn, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Cloud Native Novice]]
- País/cidade: France / Paris
- Speakers: Flynn, Buoyant
- Schedule: https://kccnceu2024.sched.com/event/1YeOy/the-rustvolution-how-rust-is-the-future-of-cloud-native-flynn-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=The+Rustvolution%3A+How+Rust+Is+the+Future+of+Cloud+Native+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The Rustvolution: How Rust Is the Future of Cloud Native.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOy/the-rustvolution-how-rust-is-the-future-of-cloud-native-flynn-buoyant
- YouTube search: https://www.youtube.com/results?search_query=The+Rustvolution%3A+How+Rust+Is+the+Future+of+Cloud+Native+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2q3RLffSvEc
- YouTube title: The Rustvolution: How Rust Is the Future of Cloud Native - Flynn, Buoyant
- Match score: 0.967
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-rustvolution-how-rust-is-the-future-of-cloud-native/2q3RLffSvEc.txt
- Transcript chars: 28502
- Keywords: pointers, pointer, compiler, actually, reference, language, ownership, languages, static, garbage, explicit, compile, another, pretty, write, little, memory, probably

### Resumo baseado na transcript

all right I guess we'll go ahead and get started I'm Flynn I'm a tech evangelist with buyant I mostly work on the open source side of linker in a previous life I was the original author of The Emissary English Gateway but now I work in marketing so everybody has filled the room to listen to a marketer talk about a programming language I am going to talk about why rust is the future of a cloud native but to do that I'm going to start in the past to be explicit making things explicit is harder up front you have to go to more work it will cost you more effort but then it will pay dividends for the rest of your life and possibly more importantly it will pay dividends for the

### Excerpt da transcript

all right I guess we'll go ahead and get started I'm Flynn I'm a tech evangelist with buyant I mostly work on the open source side of linker in a previous life I was the original author of The Emissary English Gateway but now I work in marketing so everybody has filled the room to listen to a marketer talk about a programming language I am going to talk about why rust is the future of a cloud native but to do that I'm going to start in the past in 1996 at the operating systems design and implementation conference in Seattle where in the vendors Hall at one point I ended having ended up having a conversation for about half an hour with a guy with white hair and a white beard and a name tag that said Dennis Richie if you are not familiar with this guy and many of you may not be he was the inventor of the C programming language he co-invented Unix which means that he pretty much kickstarted what we're doing here in this industry today and in the process he brought us Decades of buffer overruns and security violations and cves and countless hours and dollars lost ripping our Collective hair out trying to figure out what was going on with our programs that's honestly the biggest thing I remember about that conversation he was very Charming he was clearly brilliant nice guy great conversationalist and it was very very difficult to reconcile in my head all the amazing stuff he'd done and all the incredible pain that had gone along with it so this talk is pretty much about how we do better and about why that's important I'm starting with C because it has been massively influential on all the tools that we use today and that influence should not be understated but it was written for a very different time when it was written in 1972 the industry believed that programmers could write code that was correct and that they would not write code that was malicious and we know that both of these things are false at this point that we as people working in a programming language will make every single mistake the language will allow us to make eventually and we know that there are some people who are going to write malicious code that was not the world that C was written in so the end result is that c and C++ are fast but they have no safety in some of you may be thinking oh C+ plus is safer than C no it is not and we'll come back to that I will fight you there are a bunch of other languages that make different trade-offs right we have this interpreted languages that tend to
