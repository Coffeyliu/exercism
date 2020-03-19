use cpython::{PyResult, Python, py_module_initializer, py_fn};
use std::collections::HashMap;

py_module_initializer!(rustpylib, initrustpylib, PyInit_rustpylib, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    m.add(py, "rust_word_count", py_fn!(py, rust_word_count(sentence: &str)))?;
    Ok(())
});

fn count_words(mut acc: HashMap<String, i32>, word: &str) -> HashMap<String, i32> {
    {
        let c = acc.entry(word.to_string()).or_insert(0);
        *c += 1;
    }

    acc
}

fn rust_word_count(_: Python, sentence: &str) -> PyResult<HashMap<String, i32>> {
    Ok(sentence.to_lowercase().split(|c: char| !c.is_alphanumeric() && c != '\'')
       .map(|w| w.trim_matches('\''))
       .filter(|w| !w.is_empty())
       .fold(HashMap::new(), count_words))
}
