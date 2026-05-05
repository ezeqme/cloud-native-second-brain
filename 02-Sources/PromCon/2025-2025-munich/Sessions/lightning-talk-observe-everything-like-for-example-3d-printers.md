---
type: session
event: "PromCon EU 2025"
year: 2025
kind: session
youtube_url: "https://www.youtube.com/watch?v=ZBgM402Tay0"
youtube_id: "ZBgM402Tay0"
playlist: "PromCon EU 2025"
playlist_id: "PLj6h78yzYM2P534LgwCVm3GQdxLcSt7We"
playlist_index: 42
speakers: ["Pavel Strobl"]
topics: ["OpenTelemetry", "Metrics", "Tracing", "Logging", "AI Observability"]
keywords: ["metrics", "prometheus", "logs", "opentelemetry", "exporter", "always", "exporters", "printers", "looking", "everything", "expose", "grafana", "language", "whatever", "laughter", "hardware", "observe", "others", "encourage", "cannot", "programming", "actually", "absolutely", "awesome"]
transcript_file: "_sources/transcripts/youtube-playlists/promcon-eu-2025/lightning-talk-observe-everything-like-for-example-3d-printers/ZBgM402Tay0.txt"
transcript_chars: 4102
status: "transcript-downloaded"
match_score: 1.08
---

# Lightning Talk: Observe everything! Like... for example 3D printers - Pavel Strobl

## Metadata

- YouTube: https://www.youtube.com/watch?v=ZBgM402Tay0
- Playlist: PromCon EU 2025
- Speakers: Pavel Strobl
- Topics: [[OpenTelemetry]], [[Metrics]], [[Tracing]], [[Logging]], [[AI Observability]]

## Transcript

Okay, good evening everyone. My talk is not a technical as the others were. I'm here more like to encourage you to observe everything. For example, 3D printers. You can ask but why? I don't need more metrics in my life, you know. I have node exporter, you know. I always say that it's not about why, but why not? Okay, not it's not me, but you know. You should ask yourself what you enjoy. If you enjoy, I don't know, skydiving, if you enjoy driving, if you enjoy, I don't know what, playing Call of Duty and Battlefield. Uh Then you can expose metrics from things you cannot imagine. And the answer is always yes, of course. Me, I like programming. Doesn't mean I'm good programmer, but I like it. I enjoy 3D printing. Doesn't mean I'm good 3D printer. I like seeing stuff in Grafana. So I started writing Prusa exporter. Don't look at the code, please. I will just learn Go language. How hard could it be? Yeah. Me being from object-oriented programming wasn't that easy.

However, it's always about learning new stuff. So it was like this. And you can actually help someone with the metrics that you exposed, which actually happened to me. I helped one researcher from German university to do research about our printers, which is absolutely awesome. Uh If you can consider I'm looking at you. Consider open sourcing your project. If you can, of course, not possible always inside company, and that's not always possible. So metrics from printers, right? Yes. Uh Why not? Prusa exporter demo is Grafana Goof. You can take a look. Written in Go language and using Prometheus 3.7, not 3.1, as metrics backend. So I'm going to take a look at the smooth rate function. And Grafana for visualization, but it's Prometheus. You can just take the data and do whatever you want with them. This is like self-promo, right? Yes and no. Uh Basically, I want to encourage you to create stuff. And I have few interesting exporters.

OBD exporters, if you know cars, you can have a little dongle and just get data from your car. CS:GO, that's not anymore, unfortunately. But you could get data from Counter-Strike Global Offensive. DayZ, never played it, so I don't know. NFS exporter, that's not Need for Speed. And I was looking for Call of Duty exporters and I found nothing. But yeah, there's a lot of exporters in the wild that doesn't even anybody knows about. And you can just take a look and maybe you'll find what you're looking for. And if you don't, then just write it. It doesn't have to be Go language. It can be Python. It can be whatever. PHP. >> [laughter] >> What should I do? You have two options. If you're operating like observing hardware that you haven't built, you can write exporter. Are you Are you brewing beer? Yes, if you throws all one systems, sometimes expose Wi-Fi. And you can get the something from them. Growing stuff, of course, soil sensors, of course.

Front controllers, because why not? Everything that can be somehow is your playground. You can just use the JSON exporter with if it's REST API. And don't be afraid to combine exporters. You can have GPS data and OBD exporter. This is If you are brewing, then you know what is it. This is basically monitoring the activity of yeast. And this is absolutely awesome that I found the model of at Printables. I was just looking for the model. One minute, I know. >> [laughter] >> But thanks. Anyway, you can just download the code and upload it. This is for the CS:GO. >> [laughter] >> Take whatever you want from that. And yeah, the second way is to instrument your application or your hardware. You can just on the level of the hardware software write to expose not only metrics, but also logs, traces, a lot of stuff you can use with OpenTelemetry. And of course, it's Prometheus. Uh It's more than node exporter. It's fun.

It can be useful. It can change your life. You can help others. Cannot summon the electric lord, unfortunately. But think about your target audience, audience because that's where I kind of screw up because I represent export of basically for the book. The uh the book guys. Okay. So, you just do it.


## Related keywords

[[metrics]] [[prometheus]] [[logs]] [[opentelemetry]] [[exporter]] [[always]] [[exporters]] [[printers]] [[looking]] [[everything]] [[expose]] [[grafana]]

## Notes

- Raw note imported from CNCF YouTube playlist. Promote durable insights to topic notes under `03-Topics/`.
