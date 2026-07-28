# Исходные материалы

## `docx`

`docx` версии РПД, ФОС, ЛР

## `md`

`Markdown` версии [`docx` документов](#docx), полученные при помощи `pandoc`.

Остальные документы должны ссылаться на эти `Markdown` версии для удобства предпросмотра и навигации.

### Генерация `md`

```terminal
nix develop --command sh -c 'for source in source-materials/docx/fos/*.docx source-materials/docx/labs/*.docx source-materials/docx/rpd/*.docx; do target="${source/source-materials\/docx/source-materials\/md}"; pandoc --from=docx --to=gfm --wrap=none --output="${target%.docx}.md" "$source" || exit; done'
```

## Версионирование

Мы используем [SemVer](https://semver.org/lang/ru/) для обозначения версий документов.

Части репозитория могут быть основаны на не самой последней версии документов. Нам нужно обновлять репозиторий до последней версии. Поэтому мы храним и старую, и новую версию документов.
